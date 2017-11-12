import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8080/")

while (True):
	print proxy.consume()