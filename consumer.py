import xmlrpclib
import time
proxy = xmlrpclib.ServerProxy("http://localhost:8080/")

print "The Consumer connected the server"

sentence = proxy.consume()

while True :
	print "The consume was :" + sentence
	time.sleep(2)