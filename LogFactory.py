# -*- coding: utf-8 -*-
# !/usr/bin/env python
import logging
import Config


# Return the logger with specified log conifg in basic config file
def logger(name, config):
    log_config = config.readLogConfig()
    logger = logging.getLogger(name)
    fh = logging.FileHandler(log_config['log_path'] + "/" + log_config['log_name'])
    fh.setLevel(log_config['log_level'])
    formatter = logging.Formatter(log_config['log_format'])
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
