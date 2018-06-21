#-*- coding:UTF-8 -*-
#pyhthon36
import socket  
import os,struct

HOST = '202.199.6.212'  
PORT = 2047 
  
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.connect((HOST,PORT))  
while True:

	filepath = input('input your filepath:\r\n')
	if os.path.isfile(filepath):
		#定义打包规则
		fileinfo_size = struct.calcsize('128sl')
		filename = os.path.basename(filepath)
		b_filename = bytearray(filename,'UTF-8')
		filesize = os.stat(filepath).st_size
		#定义文件头信息，包含文件名和文件大小
		fhead = struct.pack('128sl',b_filename,filesize)
		s.send(fhead)
		print('client filepath:', filepath)
		# with open(filepath,'rb') as fo: 这样发送文件有问题，发送完成后还会发一些东西过去
		fo = open(filepath,'rb')
		while True:
			filedata = fo.read(1024)
			if not filedata:
				break
			s.send(filedata)
		fo.close()
	else:
		print('not send file')
	# 	print('send over...')
	# input_data = input('path:')
	# path,file_name = os.path.split(input_data)
	# file_size = os.stat(path).st_size
	# s.send((path+"//"+file_name+"//"+str(file_size)).encode())
	# send_size = 0
	# f = open(input_data,'rb')
	# Flag = True
	# while Flag:
	# 	if send_size + 1024 > file_size:
	# 		data = f.read(file_size - send_size)
	# 		Flag = False
	# 	else:
	# 		data = f.read(1024)
	# 		send_size += 1024
	# 	s.send(data)
	# f.close()
	# print('send over...')
# s.close() 