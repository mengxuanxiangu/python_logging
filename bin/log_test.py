#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Inc. All Rights Reserved
# 
########################################################################
 
"""
File: log_test.py
Author: mengxuanxiangu(mengxuanxiangu@gmail.com)
Date: 2017/03/03 11:54:25
"""

import time
from log import logger

while True:
    logger.info('info test')
    logger.debug('debug test')
    logger.error('error test')
    logger.critical('critical test')
    logger.warn('warn test')
    time.sleep(1)
