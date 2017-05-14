# -*- coding: utf-8 -*-
# !/usr/bin/env python
import LogFactory
import logging
import Config

import web
import subprocess
import os

# Get logger
_logger = LogFactory.logger("Groot.Server")
_logger.setLevel(logging.DEBUG)
_logger.info("Initializing Groot Web Server")

# Prepare web server, urls pattern
_render = web.template.render('templates/')
_urls = (
    '/', 'indexHandler',
    '/stopme', 'stopMyselfHandler',
    '/puppet/refresh', 'puppetRefreshHandler',
    '/puppet/list', 'puppetListHandler',
)
app = web.application(_urls, globals())


# Start web server
def start():
    web.webapi.config.debug = False
    _logger.info(" ***** Groot Web Server starting up!")
    app.run()


# Stop web server
def stop():
    app.stop()
    _logger.info(" ***** Groot Web Server stopped.")


# Handlers
class indexHandler:
    def GET(self):
        return _render.index()


class stopMyselfHandler:
    def GET(self):
        _logger.info("Client {ip} is trying to stop me...".format(ip=web.ctx.ip))
        stop()
        return "OK"


class puppetRefreshHandler:
    def GET(self):
        # Get Puppet config
        _logger.info("Read Puppet config.")
        puppet_path = Config.BasicConfig.readPuppetConfig()["puppet_path"]
        # Execute git pull
        result = subprocess.call(['../bin/get_latest.sh', '-p', puppet_path])
        _logger.info("Get latest puppet modules from Git.")
        # Handle bash results
        if result == 0:
            _logger.info("Git pull successfully.")
            return "OK"
        else:
            _logger.error("Fail to git pull latest puppet modules.")
            return "Fail"


class puppetListHandler:
    def GET(self):
        # Get Puppet config
        _logger.info("Read Puppet config.")
        modules_path = Config.BasicConfig.readPuppetConfig()["puppet_modules"]
        modules = os.walk(modules_path).next()[1]
        _logger.info("Get current Puppet modules. Modules List:\n" +
                     "**********************************************************************************\n"
                     "{modules}\n".format(modules=modules) +
                     "**********************************************************************************")
        # Store modules in cache
        return modules
