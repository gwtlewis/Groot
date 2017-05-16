# -*- coding: utf-8 -*-
# !/usr/bin/env python
from Groot import server
import web
import subprocess
import os


class indexHandler(server):
    def GET(self):
        return self._render.index()


class stopMyselfHandler(server):
    def GET(self):
        self._logger.info("Client {ip} is trying to stop me...".format(ip=web.ctx.ip))
        self.stop()
        return "OK"


class puppetRefreshHandler(server):
    def GET(self):
        # Get Puppet config
        self._logger.info("Read Puppet config.")
        puppet_path = self.config.readPuppetConfig()["puppet_path"]
        # Execute git pull
        result = subprocess.call([self.base_path + '/bin/get_latest.sh', '-p', puppet_path])
        self._logger.info("Get latest puppet modules from Git.")
        # Handle bash results
        if result == 0:
            self._logger.info("Git pull successfully.")
            return "OK"
        else:
            self._logger.error("Fail to git pull latest puppet modules.")
            return "Fail"


class puppetListHandler(server):
    def GET(self):
        # Get Puppet config
        self._logger.info("Read Puppet config.")
        modules_path = self.config.readPuppetConfig()["puppet_modules"]
        modules = os.walk(modules_path).next()[1]
        self._logger.info("Get current Puppet modules. Modules List:\n" +
                          "**********************************************************************************\n"
                          "{modules}\n".format(modules=modules) +
                          "**********************************************************************************")
        # Store modules in cache
        return modules