import socket
import threading
#port number
port = 3306
#socket installation
server = socket.socket()

#hostname
hostnme = socket.gethostname()

#server connection
server.bind((server,port))
server.listen(5)

#server ready 
print("!!!Server ready to work!!!")

#number of clients
clients = []

#broadcast to every client
def broadcast_message():
   pass

#chat between two
def chat_between_two():
   pass

#
while True:
   conn,addr=server.accept()
    