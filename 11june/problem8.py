import subprocess
command_input=input("Enter command:")
attribute_input=input("Enter attribute:")
command=[command_input,attribute_input]

f=open('clog.txt','a')
f.write(command_input+attribute_input)
f.close()

process= subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,error=process.communicate()
o=output.decode('ascii')
print(o)
