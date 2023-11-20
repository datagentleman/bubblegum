import numpy as np
from starbucks.client import Client

HOST = '127.0.0.1'
PORT = 1337

if __name__ == '__main__':
  client = Client(HOST, PORT).connect()

  data = np.arange(200, dtype=np.int32).tobytes()
  client.send("TPUT", "tensors/iris/1.bucket", data)
  
  print(client.read('bytes'))