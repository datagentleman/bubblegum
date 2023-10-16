import socket
from starbucks.packet import Message as msg

HOST = '127.0.0.1'
PORT = 1337

if __name__ == '__main__':
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((HOST, PORT))
      
      while True:
        cmd = input("cmd: ")
        print(f"Data send: {cmd.encode()}")
        msg.send(s, cmd)
        print(msg.recv(s))
        