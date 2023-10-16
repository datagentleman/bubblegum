import socket
import starbucks.packet as packet

HOST = '127.0.0.1'
PORT = 1337

if __name__ == '__main__':
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((HOST, PORT))
      
      while True:
        cmd = input("cmd: ")
        print(f"Data send: {cmd.encode()}")
        packet.write(s, cmd.encode())
        print(packet.read(s))
        