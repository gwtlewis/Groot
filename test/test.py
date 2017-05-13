# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os
import sys

import Config
import Logger


class test(object):
    log = Config.BasicConfig.readLogConfig()
    print log["log_name"]

    print Logger