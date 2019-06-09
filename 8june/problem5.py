import datetime
name=input("Enter your name :")
time=datetime.datetime.now().hour
print(time)
if(time<12):
    print("Hello {}, Good Morning !".format(name))
elif(time >12 and time <16):
    print("Hello {}, Good Afternoon !".format(name))
elif (time>16 and time <21) :
    print("Hello {}, Good Evening".format(name))
else:
    print("Hello {}, Good Night".format(name))

