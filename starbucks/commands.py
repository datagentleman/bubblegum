from starbucks.stream  import Stream
from starbucks.dataset import Dataset  
from starbucks.worker  import Worker  
from starbucks.buffer  import Buffer  

def hello(args, stream: Stream):
  stream.send(b"Another latte?")


def stream(args, stream: Stream=None):
  dataset_name = args[0]
  data = Dataset.read(dataset_name)

  # Temporary - only for development
  buf = Buffer().write(data)
  return data if stream == None else stream.send(buf)


def worker_ls(args=None, stream: Stream=None):
  buf = Buffer()

  [buf.write(name.encode()) for name in Worker.ls()]
  stream.send(buf)


def worker_run(args=None, stream: Stream=None):
  res = Worker('give_me_all_the_data').run()
  stream.send(Buffer().write("Worker is running".encode()))
