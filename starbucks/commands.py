from starbucks.stream  import Stream
from starbucks.dataset import Dataset  
from starbucks.worker  import Worker  

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
  
  
def worker_list(args=None, stream: Stream=None):
  data = b''.join((name.encode() for name in Worker.ls()))
  stream.send(data)