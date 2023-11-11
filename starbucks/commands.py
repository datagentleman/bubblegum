from starbucks.stream      import Stream
from starbucks.conn        import Conn
from starbucks.worker      import Worker  
from starbucks.buffer      import Buffer  
from starbucks.tensor      import Tensor  
from starbucks.data_stream import DataStream

def response(code: str, msg: str="")-> Buffer:
  return Buffer().write(code.encode()).write(msg.encode())


def hello(args, conn: Conn):
  conn.send(Buffer().write(b'Another latte?'))


### 
### WORKERS
###

# list all workers
def worker_ls(args, conn: Conn):
  buf = Buffer()

  [buf.write(name.encode()) for name in Worker.ls()]
  conn.send(buf)


# run worker
def worker_run(args, stream: Stream):
  name = args[0]
  Worker(name).run()
  stream.send(response('OK'))


### 
### TENSORS 
###

# create tensor
def tensor_create(args, stream: Stream):
  tensor = args[0]

  try:
    Tensor.create(tensor)
    stream.send(response('OK'))
  except Exception as e:
    stream.send(response('ERROR', str(e)))

  
# list all tensors
def tensor_list(args, stream: Stream):
  buf = Buffer()

  try:
    [buf.write('/'.join(tensor).encode()) for tensor in Tensor.ls()]
    stream.send(buf)
  except Exception as e:
    stream.send(response('ERROR', str(e)))


# remove tensor
def tensor_remove(args, stream: Stream):
  tensor = args[0]

  try:
    Tensor.remove(tensor)
    stream.send(response('OK'))
  except Exception as e:
    stream.send(response('ERROR', str(e)))


# stream tensor
def tensor_stream(args, stream: Stream):
  tensor = Tensor.find(args[0])
  if not tensor: return
  
  iter = tensor.iter()
  ds   = DataStream(stream)

  while True:
    if not ds.write(iter.next()):
      break
    