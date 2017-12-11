#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""

import pika
# tcp连接
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
# 创建channel连接
channel = connection.channel()
# print(channel)
channel.queue_declare(queue="one")
channel.basic_publish(exchange="",
                      routing_key="one",
                      body="this one")
print("send this one by one")
connection.close()