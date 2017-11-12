import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8080/")

proxy.produce("oi")