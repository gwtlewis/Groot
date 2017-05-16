# -*- coding: utf-8 -*-
# !/usr/bin/env python
import LogFactory
import logging
import Config
import web


class server(object):
    def __init__(self, base_path):
        self.base_path = base_path

        # Get logger
        self._logger = LogFactory.logger("Groot.Server")
        self._logger.setLevel(logging.DEBUG)
        self._logger.info("Initializing Groot Web Server")

        # Prepare web server, urls pattern
        self._render = web.template.render(base_path + 'templates/')
        self._urls = (
            '/', 'Handlers.indexHandler',
            '/stopme', 'Handlers.stopMyselfHandler',
            '/puppet/refresh', 'Handlers.puppetRefreshHandler',
            '/puppet/list', 'Handlers.puppetListHandler',
        )
        self.app = web.application(self._urls, globals())
        self.config = Config.BasicConfig(base_path)

    # Start web server
    def start(self):
        web.webapi.config.debug = False
        self._logger.info(" ***** Groot Web Server starting up!")
        self.app.run()

    # Stop web server
    def stop(self):
        self.app.stop()
        self._logger.info(" ***** Groot Web Server stopped.")



