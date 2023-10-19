from starbucks.client import Client

HOST = '127.0.0.1'
PORT = 1337

def get_me_all_data(input):
  print(f"Got data from node: {input}")


if __name__ == '__main__':
  stream = Client(HOST, PORT)
  stream.send("STREAM", "iris/iris.csv")
  
  get_me_all_data(stream.read())
  