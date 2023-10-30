import sys

from starbucks.client import Client
from starbucks.config import Config as config

config.load()
HOST = config["server"]["host"]
PORT = config["server"]["port"]

# exec user defined worker function
exec(sys.argv[1])

if __name__ == '__main__':
  client = Client.connect(HOST, PORT)  
  iter   = client.tstream('iris')

  # Call user defined perform() function. 
  perform = getattr(sys.modules[__name__], 'perform')
  perform(iter)
  