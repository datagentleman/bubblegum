from starbucks.stream   import Stream
from starbucks.datasets import Dataset  

def hello(args, stream: Stream):
  stream.send(b"Another latte?")


def stream(args, stream: Stream=None):
  dataset_name = args[0]
  data = Dataset.read(dataset_name)
  
  
  # Temporary - only for development
  if stream == None:
    return data
  else:
    stream.send(data)
    
  