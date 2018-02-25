import socket
import sys

# usage lightTest.py <command> <address of Pi> <port on Pi>
# a command of 'good' will trigger a good animation
# a command of 'bad' will trigger a bad animation
# a command of 'idle' will trigger the idle animation
# all other commands will trigger an error animation

message = str(sys.argv[1])
address = str(sys.argv[2])
port = str(sys.argv[3])

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((address, port))
clientsocket.send(message)
