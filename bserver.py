#Back End server 

from socket import *

Host = '172.16.31.76'
Port = 7003
# Port = 4002
socket1 = socket(AF_INET, SOCK_DGRAM)
socket1.bind((Host,Port))
connectedClients=[]
print("Active",str(Port))

while 1:
	#print(connectedClients)
	data, address = socket1.recvfrom(2048)
	data = data.decode()
	request = data.split("!")
	if request[0] == "add":
		new_client = eval(request[1])
		if new_client not in connectedClients:
			connectedClients.append(new_client)
	elif request[0] == "message":
		print(data)
		for i in range(len(connectedClients)):
					if (connectedClients[i] != eval(request[1])):
						socket1.sendto((request[1]+":"+request[2]).encode(),connectedClients[i])
	elif request[0] == "SYN-SENT":
		socket1.sendto("SYN-RECEIVED".encode(), address)
	else:
		print("no case matched")
