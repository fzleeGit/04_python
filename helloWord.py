
import logging  # 引入logging模块
import os.path
import time
 
#1、创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关
 
#2、创建一个handler，用于写入日志文件

rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.dirname(os.path.realpath(__file__)) + '/Logs/'
log_name = log_path + rq + '.log'
logfile = log_name
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
 
#3、定义handler的输出格式
formatter = logging.Formatter("%(asctime)s,%(message)s")
fmt = logging.Formatter('%(asctime)s,%(message)s', '%Y-%m-%d %H:%M:%S')
fmt3 = logging.Formatter('%(asctime)s,%(message)s')
fh.setFormatter(fmt3)
 
#4、将logger添加到handler里面
logger.addHandler(fh)
 
#5、输出日志
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')
