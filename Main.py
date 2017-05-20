# -*- coding: utf-8 -*-
# !/usr/bin/env python
import logging
import os
import subprocess
from optparse import OptionParser
import web
import Utils

import Config
import LogFactory

# Get input option
parser = OptionParser()
parser.add_option("-b", "--base-path", dest="base_path")
(options, args) = parser.parse_args()

if not options.base_path:
    raise Exception("Option --base-path missing.")

# Initialize configuration
config = Config.BasicConfig(options.base_path)

# Initialize logger
logger = LogFactory.logger("Groot.Server", config)
logger.setLevel(logging.DEBUG)

# Initialize web.py application
logger.info("Initializing Groot Web Server")
render = web.template.render('templates/')
urls = (
    '/', 'indexHandler',
    '/stopme', 'stopMyselfHandler',
    '/puppet/refresh', 'puppetRefreshHandler',
    '/puppet/list', 'puppetListHandler',
    '/puppet/c', 'puppetCompile',
)
app = web.application(urls, globals())

# Initialize Utils
utils = Utils.utils()


# Start web server
def grootStart():
    web.webapi.config.debug = False
    app.run()
    logger.info(" ***** Groot Web Server start up!")


# Stop web server
def grootStop():
    app.stop()
    logger.info(" ***** Groot Web Server stopped.")


# Request handlers
class indexHandler:
    def GET(self):
        return render.index()


class stopMyselfHandler:
    def GET(self):
        logger.info("Client {ip} is trying to stop me...".format(ip=web.ctx.ip))
        grootStop()
        return "OK"


class puppetRefreshHandler:
    def GET(self):
        # Get Puppet config
        logger.info("Read Puppet config.")
        puppet_path = config.readPuppetConfig()["puppet_path"]
        # Execute git pull
        result = subprocess.call([options.base_path + '/bin/get_latest.sh', '-p', puppet_path])
        logger.info("Get latest puppet modules from Git.")
        # Handle bash results
        if result == 0:
            logger.info("Git pull successfully.")
            return "OK"
        else:
            logger.error("Fail to git pull latest puppet modules.")
            return "Fail"


class puppetListHandler:
    def GET(self):
        # Get Puppet config
        logger.info("Read Puppet config.")
        modules_path = config.readPuppetConfig()["puppet_modules"]
        modules = os.walk(modules_path).next()[1]
        logger.info("Get current Puppet modules. Modules List:\n" +
                    "**********************************************************************************\n"
                    "{modules}\n".format(modules=modules) +
                    "**********************************************************************************")
        # Store modules in cache
        return modules


class puppetCompile:
    def GET(self):
        inputs = web.input(module=[])
        moduleName = inputs.module[0]
        logger.info("Going to compile module: " + moduleName)
        module_full_path = os.path.join(config.readPuppetConfig()['puppet_modules'], moduleName)
        try:
            output = subprocess.check_output(['puppet', 'apply', module_full_path, '--noop', '--verbose'])
            logger.info('Compilation succeed for {}.\n'
                        'Output messages:'.format(moduleName))
            logger.info(output)
            # Remove terminal highlight
            return utils.escapeAnsiTerminalCodes(output)
        except subprocess.CalledProcessError as e:
            logger.error('Somthing wrong when compiling {}, error message:\n{}.'.format(moduleName, e.output))
            return "Fail to compile."


if __name__ == "__main__":
    grootStart()
