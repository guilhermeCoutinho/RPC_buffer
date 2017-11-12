import xmlrpclib

import time
proxy = xmlrpclib.ServerProxy("http://localhost:8080/")

print "The Consumer connected the server"

while True :
	sentence = proxy.consume()
	print "The consume was :" + sentence
	time.sleep(2)