# -*- coding: utf-8 -*-
# !/usr/bin/env python
import LogFactory
import logging


class Server(object):
    def __init__(self):
        self.logger = LogFactory.logger("Groot.Server")
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("Initializing Groot Web Server")

    def start(self):
        self.logger.info("Groot Web Server started up!")


if __name__ == "__main__":
    groot = Server()
    groot.start()


