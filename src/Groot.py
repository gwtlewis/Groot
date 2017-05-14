# -*- coding: utf-8 -*-
# !/usr/bin/env python
import LogFactory
import logging
import Config

import web
import subprocess

# Get logger
_logger = LogFactory.logger("Groot.Server")
_logger.setLevel(logging.DEBUG)
_logger.info("Initializing Groot Web Server")

# Prepare web server
_render = web.template.render('../templates')
_urls = (
    '/', 'indexHandler',
    '/git/refresh', 'gitRefreshHandler',
)
app = web.application(_urls, globals())


# Start web server
def start():
    web.webapi.config.debug = False
    app.run()
    _logger.info("Groot Web Server started up! Please enjoy the service")


# Handlers
class indexHandler:
    def GET(self):
        return _render.index()


class gitRefreshHandler:
    def GET(self):
        # Get Puppet config
        logging.info("Read Puppet config.")
        puppet_path = Config.BasicConfig.readPuppetConfig()["puppet_path"]
        # Execute git pull
        result = subprocess.call(['../bin/get_latest.sh', '-p', puppet_path])
        logging.info("Get latest puppet modules from Git.")
        # Handle bash results
        if result == 0:
            logging.info("Git pull successfully.")
            return "OK"
        else:
            logging.error("Fail to git pull latest puppet modules.")
            return "Fail"
