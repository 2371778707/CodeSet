#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""
import  pika
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="one")


def callback(ch, method, properties, body):
    print(
    " [x] Received %r" % (body,))
    ch.basic_ack(delivery_tag = method.delivery_tag)
channel.basic_consume(callback,
                      queue='one',
                      )

channel.start_consuming()
