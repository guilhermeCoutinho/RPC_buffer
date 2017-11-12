import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading

BUFFER_SIZE = 3
indexBuffer = -1

mutex = threading.Semaphore(1)

buffer = range(BUFFER_SIZE)

server = SimpleXMLRPCServer(("localhost", 8080))

def Store (data):
	global mutex,indexBuffer
	mutex.acquire()
	if (indexBuffer == BUFFER_SIZE - 1):
		mutex.release()
		return "full buffer"
	else:
		indexBuffer += 1
		buffer[indexBuffer] = data
		print ("Armazenei " + data)
		mutex.release()
		return "Sucesso"

def Consume ():
	global mutex,indexBuffer
	mutex.acquire()
	if (indexBuffer == -1):
		mutex.release()
		return "empty buffer"
		print "empty buffer"
	else :
		indexBuffer -= 1
		print (indexBuffer)
		mutex.release()
		print "Item consumido " + buffer[indexBuffer + 1]
		return (buffer[indexBuffer+1] )

server.register_function(Store, "produce")
server.register_function(Consume, "consume")
print "Server up and running"
server.serve_forever()