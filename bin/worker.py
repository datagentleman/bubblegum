import sys

from bubblegum.client import Client
from bubblegum.config import Config as config

HOST = config["server.host"]
PORT = config["server.port"]

# exec user defined worker function
exec(sys.argv[1])

if __name__ == '__main__':
  # connect to bubblegum server
  client = Client(HOST, PORT).connect()  
  iter   = client.tstream('iris')

  while True:
    # Call user defined perform() function. 
    perform = getattr(sys.modules[__name__], 'perform')
    perform(iter)
    break
  