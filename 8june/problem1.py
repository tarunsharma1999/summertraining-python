import datetime
name=input("Enter name:")
age=int(input("your age:"))
d=datetime.datetime.now()
year=d.year
print("name:{}. \nyear in which you will turn 95: {}.".format(name,(95-age)+year))
