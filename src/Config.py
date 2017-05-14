# -*- coding: utf-8 -*-
# !/usr/bin/env python
import ConfigParser


class BasicConfig(object):
    @staticmethod
    def readLogConfig():
        config = ConfigParser.RawConfigParser()
        config.readfp(open(r'../config/basic.cfg'))
        log_level = config.get("log", "level")
        log_path = config.get("log", "path")
        log_name = config.get("log", "name")
        log_format = config.get("log", "format")
        return {"log_level": log_level,
                "log_path": log_path,
                "log_name": log_name,
                "log_format": log_format}

    @staticmethod
    def readPuppetConfig():
        config = ConfigParser.RawConfigParser()
        config.readfp(open(r'../config/basic.cfg'))
        return {"puppet_path": config.get("puppet", "repo"),
                "puppet_modules": config.get("puppet", "modules")}
