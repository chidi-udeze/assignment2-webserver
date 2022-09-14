# import socket module
from socket import *

# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", port))
    serverSocket.listen(1)

    while True:
        connectionSocket, addr = serverSocket.accept()
        try:
          message = connectionSocket.recv(1024)
          filename = message.split()[1]
          f = open(filename[1:]) 
          outputdata = f.read()
          f.close()

          connectionSocket.send(b'HTTP/1.0 200 OK\nContent-Type: text/html\n\n')
          
          for i in range(0, len(outputdata)): 
              connectionSocket.send(outputdata[i].encode())
          connectionSocket.close() 
        except IOError:
          error = "HTTP/1.1 404 Not Found\n"
          connectionSocket.send(error.encode())
          connectionSocket.close()
          break
        except Exception:
          connectionSocket.close()
          break
    serverSocket.close()
    sys.exit() 


if __name__ == "__main__":
    webServer(13331)