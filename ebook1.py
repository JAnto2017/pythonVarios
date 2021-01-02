import os
import platform

from datetime import datetime
net =raw_input("Enter the network Address => ")
net1= net.split('.')
a='.'
net2 = net1[0]+a+net1[2]+a+net1[2]+a

st1=int(input("Enter the Starting Number => "))
en1=int(input("Enter the Last Number => "))

en1=en2 + 1
oper=platform.system()

if oper=="Windows":
    ping1="ping -n 1 " 
elif (oper== "Linux"):
    ping1 = "ping -c 1 "
else:
    ping1 = "ping -c 1"

t1=datetime.now()

print ("Scanning in Progress")

for ip in xrange(st1,en1):
    addr=net2+str(ip)
    comm=ping1+addr
    response=os.popen(comm)
    for line in response.readline():
        if 'ttl' in line.lower():
            break
        if 'ttl' in line.lower():
            print (addr,"--> Live")

t2=datetime.now()
total=t2-t1
print ("scanning complete in ",total)