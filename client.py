from starbucks.client import Client

HOST = '127.0.0.1'
PORT = 1337

if __name__ == '__main__':
  conn = Client(HOST, PORT)
  
  while True:
    cmd_name = input("cmd: ")
    conn.send(cmd_name)
    
    res = conn.read()
    print(f'RESPONSE: {res.data()}')