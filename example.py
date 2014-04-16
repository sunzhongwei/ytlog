#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.0.1"
__author__ = "Zhongwei Sun (zhongwei.sun2008@gmail.com)"

# ----------------------------------------
# Example for using log.py
# ----------------------------------------

# build-in, 3rd party and my modules
import time
from log import app_log


if '__main__' == __name__:
    app_log.info("Mission starts.")
    wait_time = 2

    while True:
        app_log.info("Wait %s seconds" % wait_time)
        app_log.debug("I'm debug.")
        app_log.warning("I'm warning.")
        app_log.error("I'm error.")
        time.sleep(wait_time)

