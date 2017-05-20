# -*- coding: utf-8 -*-
# !/usr/bin/env python
import re


class utils(object):
    @staticmethod
    def escapeAnsiTerminalCodes(line):
        ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
        return ansi_escape.sub('', line) 