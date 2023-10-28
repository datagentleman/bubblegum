from starbucks.stream  import Stream
from starbucks.dataset import Dataset  
from starbucks.worker  import Worker  
from starbucks.buffer  import Buffer  
from starbucks.tensor  import Tensor  

def response(code: str, msg: str="")-> Buffer:
  return Buffer().write(code.encode()).write(msg.encode())


def hello(args, stream: Stream):
  stream.send(b"Another latte?")


def stream(args, stream: Stream=None):
  dataset_name = args[0]
  data = Dataset.read(dataset_name)

  # POC: for now we are only returning the same data
  while True:
    req = stream.read()
        
    if len(req.data()) > 0:
      buf = Buffer().write(data)
      stream.send(buf)
    else:
      break

### 
### WORKERS
###

def worker_ls(args=None, stream: Stream=None):
  buf = Buffer()

  [buf.write(name.encode()) for name in Worker.ls()]
  stream.send(buf)


def worker_run(args=None, stream: Stream=None):
  Worker('give_me_all_the_data').run()
  stream.send(response('OK'))


### 
### TENSORS 
###

def tensor_create(args=None, stream: Stream=None):
  tensor = args[0]

  try:
    Tensor.create(tensor)
    stream.send(response('OK'))
  except Exception as e:
    stream.send(response('ERROR', str(e)))

  
def tensor_list(args=None, stream: Stream=None):
  buf = Buffer()

  try:
    [buf.write('/'.join(tensor).encode()) for tensor in Tensor.ls()]
    stream.send(buf)
  except Exception as e:
    stream.send(response('ERROR', str(e)))


def tensor_remove(args=None, stream: Stream=None):
  tensor = args[0]

  try:
    Tensor.remove(tensor)
    stream.send(response('OK'))
  except Exception as e:
    stream.send(response('ERROR', str(e)))
