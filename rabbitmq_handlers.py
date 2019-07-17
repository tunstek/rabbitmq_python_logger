import logging
import pika


class RabbitLogHandler(logging.Handler):
    def __init__(self, domain, rabbit_ip, consolidate_levels=False):
        super(RabbitLogHandler, self).__init__()

        self.domain = domain
        self.rabbit_ip = rabbit_ip
        self.consolidate_levels = consolidate_levels

        self.setLevel(logging.DEBUG)

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_ip))
        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange='logs', exchange_type='topic')

    def emit(self, record):
        log_entry = self.format(record=record)
        routing_key = 'logs.{}'.format(self.domain)
        if not self.consolidate_levels:
            routing_key += '.{}'.format(self.level_to_str(record.levelno))
        self.channel.basic_publish(exchange='logs', routing_key=routing_key, body=log_entry)
        print(" [x] Sent %r:%r" % (routing_key, log_entry))

    @staticmethod
    def level_to_str(level):
        if level == 10:
            return 'debug'
        elif level == 20:
            return 'info'
        elif level == 30:
            return 'warning'
        elif level == 40:
            return 'error'
        elif level == 50:
            return 'critical'
        else:
            return 'unknown_log_level'
