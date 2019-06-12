#!/bin/python3
import sys

for i in sys.argv:
	if i!=sys.argv[0]:
		if i[0] == '>':
			f=open(i[1:len(i)],'w')
			f.write(input("Enter content of file:\n"))
			f.close()
		else :
			f=open(i,'a+')
			f.close()
