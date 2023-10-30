from starbucks.stream      import Stream
from starbucks.worker      import Worker  
from starbucks.buffer      import Buffer  
from starbucks.tensor      import Tensor  
from starbucks.data_stream import DataStream


def response(code: str, msg: str="")-> Buffer:
  return Buffer().write(code.encode()).write(msg.encode())


def hello(args, stream: Stream):
  stream.send(b"Another latte?")

### 
### WORKERS
###

def worker_ls(args=None, stream: Stream=None):
  buf = Buffer()

  [buf.write(name.encode()) for name in Worker.ls()]
  stream.send(buf)


def worker_run(args=None, stream: Stream=None):
  name = args[0]
  Worker(name).run()
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


def tensor_stream(args, stream: Stream) -> None:
  tensor = Tensor.find(args[0])
  if tensor == None: return
  
  iter = tensor.iter()
  ds   = DataStream(stream)

  while True:
    if not ds.write(iter.next()):
      break
    