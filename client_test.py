#!/usr/bin/env python
#-*- coding:utf-8 -*-

'a socket example which send echo message to server'
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8000))


#接收欢迎消息
print s.recv(1024)
for data in [b'Michael',b'Tracy',b'Sarah']:
	#发送数据
	s.send(data)
	print s.recv(1024)
s.send('exit')
s.close()