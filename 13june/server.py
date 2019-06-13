#!/usr/bin/python2
import socket,sys
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="127.0.0.1"
port =8889 
options=''' 1 to send a message.\t2 to send a file.'''
print(options)
choice=int(input("Enter your choice:"))
print(" press $ to terminate!\n")
if choice==1:
	while 4>2:
		msg=raw_input("Enter a message:")
		s.sendto(msg,(ip,port))
		data=s.recvfrom(5)
		print(data[0])
		if data[0] == '$' or msg=='$':
			exit()
elif choice==2:
	print("asd")
else :
	print("Enter valid choice!")

s.close()



