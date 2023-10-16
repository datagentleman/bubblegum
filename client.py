import socket
import starbucks.protocol 

HOST = '127.0.0.1'
PORT = 1337

if __name__ == '__main__':
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((HOST, PORT))
      
      starbucks.protocol.write(s, b'Hello')
      data = starbucks.protocol.read(s)
      print(data)