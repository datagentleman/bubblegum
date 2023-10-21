from starbucks.client import Client

HOST = '127.0.0.1'
PORT = 1337

if __name__ == '__main__':
  conn = Client(HOST, PORT)
  
  # while True:
  # cmd_name = input("cmd: ")
  conn.send("WORKER_RUN", "give_me_all_the_data")
  buf = conn.read()
  print(f'RESPONSE: {buf.data()}')