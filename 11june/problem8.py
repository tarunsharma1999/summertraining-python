import subprocess
command_input=input("Enter command:")

command=[command_input]

process= subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,error=process.communicate()
o=output.decode('ascii')
print(o)
f=open('clog.txt','w')
f.write(command_input)
f.close()
