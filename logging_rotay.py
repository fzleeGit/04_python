#!/usr/bin/env python
#_*_coding:utf-8_*_
# vim : set expandtab ts=4 sw=4 sts=4 tw=100 :

import logging
import time
import re
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

def main():
    #日志打印格式
    #log_fmt = '%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s,'
    log_fmt = '%(asctime)s,%(message)s'
    log_fmt = '%(asctime)s,%(message)s'
    formatter = logging.Formatter(log_fmt)
    #创建TimedRotatingFileHandler对象
    log_file_handler = TimedRotatingFileHandler(filename="ds_update", when="D", interval=1, backupCount=10)
    #log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    #log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)    
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger()
    log.addHandler(log_file_handler)
    #循环打印日志
    log_content = "test log"
    count = 0
    current = 0
    power = 1
    PQ = 0.5
    
    records = {count,current,power}
    while count < 100000:
        #log.error(count,current,current,power)
        #log.info(power)
        log.info('%d,%d,%d,%0.2f',count,current,power,PQ)
        records = count,current,power,PQ
        time.sleep(1)
        count = count + 1
        PQ = PQ + 0.1
        power = power + 1
        current = current + 1
    log.removeHandler(log_file_handler)


if __name__ == "__main__":
    main()