import logging
logging.basicConfig(level = logging.INFO)

#DEBUG  info  warning    error

n = 10
logging.debug('n = %d' % n)
logging.info('n = %d' % n)
logging.warning('n = %d' % n)
logging.error('n = %d' % n)

#遗留问题
# logging输出日志到文件