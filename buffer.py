#import socket
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
BUFFER_SIZE = 3
indexBuffer = -1

buffer = range(BUFFER_SIZE)

server = SimpleXMLRPCServer(("localhost", 8080))

def Store (data):
	if (indexBuffer == BUFFER_SIZE - 1):
		print "full buffer"
		return "full buffer"
	else:
		++indexBuffer
		buffer[indexBuffer] = data
		print ("Armazenei " + data)
		return "Sucesso"

def Consume ():
	if (indexBuffer == -1):
		return "empty buffer"
		print "empty buffer"
	else :
		--indexBuffer
		print "Item consumido " + buffer[indexBuffer + 1]
		return (buffer[indexBuffer+1] )

server.register_function(Store, "produce")
server.register_function(Consume, "consume")
print "Servidor rodando na porta 8080"
server.serve_forever()