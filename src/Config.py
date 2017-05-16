# -*- coding: utf-8 -*-
# !/usr/bin/env python
import ConfigParser


class BasicConfig(object):
    def __init__(self, base_path):
        self.config = ConfigParser.RawConfigParser()
        self.config.readfp(open(r'{}/basic.cfg'.format(base_path)))

    def readLogConfig(self):
        log_level = self.config.get("log", "level")
        log_path = self.config.get("log", "path")
        log_name = self.config.get("log", "name")
        log_format = self.config.get("log", "format")
        return {"log_level": log_level,
                "log_path": log_path,
                "log_name": log_name,
                "log_format": log_format}

    def readPuppetConfig(self):
        return {"puppet_path": self.config.get("puppet", "repo"),
                "puppet_modules": self.config.get("puppet", "modules")}
