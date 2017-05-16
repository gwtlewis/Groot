# -*- coding: utf-8 -*-
# !/usr/bin/env python
import Groot
from optparse import OptionParser


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-b", "--base-path", dest="base_path")
    (options, args) = parser.parse_args()
    print options.base_path
    if not options.base_path:
        raise Exception("Option --base-path missing.")

    groot = Groot.server(base_path=options.base_path)
    groot.start()
