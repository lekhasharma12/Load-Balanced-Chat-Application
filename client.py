#Multi Server Multi Client Chat Application
#FE Front End Server
#BE Back End Server

from socket import *
import threading 
import sys

server=input('Please enter IP address to connect: ') #IP Address of the FE Server
# send an empty message only during the beginning of connection

data = ''
data = data.ljust(16,'^')

Port = 7002 #Port number of the Front End Server
socket1 = socket(AF_INET, SOCK_DGRAM)
socket1.sendto(data.encode(), (server, Port))
print("----------------Chat Begins---------------------")
def transmit():
	while 1:
		data = input("\n")
		socket1.sendto(data.encode(), (server, Port))
		if data == "EXIT" or data == "exit":
			print("\nExiting chat")
			print("----------------------------------------------")
			second.stop()
			socket1.close()
			break

def get(): 
	while 1: 
		new_data, address = socket1.recvfrom(2048)
		new_data = new_data.decode()
		new_data = new_data.split(':')
		new_data2 = new_data[1]
		new_data3 = new_data[0].split(',')
		if new_data2 != '':
			print("\n"+str(new_data3[1][1:-1]) +":"+ str(new_data2))
		if new_data2 ==  "EXIT" or new_data2 == "exit":
			print("\nExiting chat")
			print("----------------------------------------------")
			first.stop()
			socket1.close()
			break

first = threading.Thread(target=transmit)
second = threading.Thread(target=get)

first.start()
second.start()
first.join()
second.join()
sys.exit()
