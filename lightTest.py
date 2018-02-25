import socket
import sys

# usage lightTest.py <message> <address of Pi> <port on Pi>

message = str(sys.argv[1])
address = str(sys.argv[2])
port = str(sys.argv[3])

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((address, port))
clientsocket.send(message)