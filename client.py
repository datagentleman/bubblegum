from starbucks.client import Client

HOST = '127.0.0.1'
PORT = 1337

if __name__ == '__main__':
  cli = Client(HOST, PORT)
  
  while True:
    cmd = input("cmd: ")
    print(f"Data send: {cmd.encode()}")

    cli.send(cmd.encode())
    print(f'RESPONSE: {cli.read()}')