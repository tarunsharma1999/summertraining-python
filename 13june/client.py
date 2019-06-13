#!/usr/bin/python2
import socket ,sys
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="127.0.0.1"
port=8889

s.bind((ip,port))
options= ''' 1 to send a message.\t2  to send a file.'''
print(options)
choice=int(raw_input("Enter your choice:"))
print("press $ to terminate!\n")
if choice ==1 :
	while 4>2 :
		data=s.recvfrom(5) 
		print("Message:"+data[0])
		msgs=raw_input("Enter a message:")
		s.sendto(msgs,data[1])
		if data[0]=='$' or msgs=='$':
			exit()		
elif choice ==2 :
	print("ASD")		
else :
	print("Enter valid option!")

s.close()
