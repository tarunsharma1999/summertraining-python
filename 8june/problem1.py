
import datetime
name=input("Enter name:")
age=int(input("your age:"))

print("name:{}. \nyear in which you will turn 95: {}.".format(name,(95-age)+datetime.datetime.now().year))
