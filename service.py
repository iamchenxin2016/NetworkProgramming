#!/usr/bin/env python
#-*- coding:utf-8 -*-
'a server example which send hello to client.'


import time
import socket
import threading


#新线程里的处理过程
def tcplink(sock,addr):
	print 'Accept new connection from %s:%s...'%addr 
	sock.send('Welcome client')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data =='exit' or not data:
			break
		sock.send('Hello client I can receive,%s！'%data)
	sock.close()
	print 'Connection from %s:%s closed.'% addr 



#创建一个基于IPV4和TCP协议的Socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#设置监听端口
s.bind(('127.0.0.1',8000))
#开始监听端口并等待连接的最大数量
s.listen(5)#监听5个客户端
print 'Waiting for connection...'

#通过永久循环来接受客户端的连接，accept()会等待并返回一个客户端的连接
while True:
#接受一个新的连接
	socket,addr = s.accept()
#创建新线程来处理TCP连接：
	t = threading.Thread(target = tcplink,args=(socket,addr))
	t.start()



