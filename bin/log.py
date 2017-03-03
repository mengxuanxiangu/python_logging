#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Inc. All Rights Reserved
# 
########################################################################
 
"""
File: log.py
Author: mengxuanxiangu(mengxuanxiangu@gmail.com)
Date: 2017/03/03 11:47:39
"""

import logging
import logging.config
import sys
import os

PATH = sys.path[0]
if os.path.isfile(PATH):
    PATH = os.path.dirname(PATH)
    os.chdir(PATH)
logging.config.fileConfig("./../conf/log.conf")
logger = logging.getLogger('main')
for handler in logger.handlers:
    if hasattr(handler, 'suffix'):
        handler.suffix="%Y%m%d%H%M%S"
