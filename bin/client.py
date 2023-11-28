import numpy as np
from starbucks.client import Client

HOST = '127.0.0.1'
PORT = 1337

if __name__ == '__main__':
  data = np.arange(10, dtype=np.int32).tobytes()
  client = Client(HOST, PORT).connect()

  res = client.tcreate("test:iris", "int16", (1), 1000, 1000)
  print(res)
  