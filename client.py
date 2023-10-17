import socket
from starbucks.stream import Stream

HOST = '127.0.0.1'
PORT = 1337

if __name__ == '__main__':
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((HOST, PORT))
      
      stream = Stream(s)
      while True:
        cmd = input("cmd: ")
        print(f"Data send: {cmd.encode()}")

        stream.send(cmd.encode())
        print(stream.read())
        