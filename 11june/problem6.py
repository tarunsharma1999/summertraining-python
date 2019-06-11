#!/bin/usr/python3
import sys

for i in sys.argv:
        if i!=sys.argv[0]:
            f=open(i,'r+')
            print(f.strip())
	    f.close()
