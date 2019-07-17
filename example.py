import logging
import rabbitmq_handlers

rabbitmq_ip = '172.17.0.2'

rh = rabbitmq_handlers.RabbitLogHandler('example', rabbitmq_ip) # defaults to sending messages as 'logs.example.debug', 'logs.example.info', etc.

logger = logging.getLogger('example')
logger.setLevel(logging.DEBUG)
logger.addHandler(rh)

logger.debug('debug test')
logger.info('info test')
logger.warning('warning test')
logger.error('error test')
logger.critical('critical test')