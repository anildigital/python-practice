# Client Program
from socket import *

host = "localhost"
port = 21567
buf = 1024
addr = (host,port)

#Create socket
UDPSock = socket(AF_INET, SOCK_DGRAM)

def_msg = "===Whatever message goes here==="
print "\n", def_msg

while (1):
  data = raw_input('>>')
       if not data:
         break
       else:
         if(UDPSock.sendto(data,addr)):
           print "Sending message  '",data,"'....."


#close socket
UDPSock.close()
