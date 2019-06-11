import sys

for i in sys.argv:
        if i!=sys.argv[0]:
            f=open(i,'a+')
            f.close()
