import xmlrpc.client as xrc

server = xrc.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

for method in server.system.listMethods():
	print(method)
	print(server.system.methodHelp(method))
	print(server.system.methodSignature(method))

data = server.phone("Bert")
print(data)
