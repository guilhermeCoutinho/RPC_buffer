import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8080/")

while (True):
	proxy.produce("oi")