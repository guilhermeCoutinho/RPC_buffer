#import socket
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
BUFFER_SIZE = 3
indexBuffer = -1

buffer = range(BUFFER_SIZE)

server = SimpleXMLRPCServer(("localhost", 1235))

def Store (data):
	if (indexBuffer == BUFFER_SIZE - 1):
		print ("full buffer")
		return "full buffer"
	else:
		buffer[++indexBuffer] = data
		print ("Armazenei " + data)
		return "Sucesso"

def Consume ():
	if (indexBuffer == -1):
		return ("empty buffer")
		print ("empty buffer")
	else :
		print ("item consumed from buffer " + buffer[indexBuffer])
		return ("Consumed from buffer " + buffer[indexBuffer--])


server.register_function(Store, "produce")
server.register_function(Consume, "consume")
server.serve_forever()