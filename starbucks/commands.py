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
def worker_run(args, conn: Conn):
  name = args[0]
  Worker(name).run()
  conn.send(response('OK'))


### 
### TENSORS 
###

# create tensor
def tensor_create(args, conn: Conn):
  tensor = args[0]

  try:
    Tensor.create(tensor)
    conn.send(response('OK'))
  except Exception as e:
    conn.send(response('ERROR', str(e)))

  
# list all tensors
def tensor_list(args, conn: Conn):
  buf = Buffer()

  try:
    [buf.write('/'.join(tensor).encode()) for tensor in Tensor.ls()]
    conn.send(buf)
  except Exception as e:
    conn.send(response('ERROR', str(e)))


# remove tensor
def tensor_remove(args, conn: Conn):
  tensor = args[0]

  try:
    Tensor.remove(tensor)
    conn.send(response('OK'))
  except Exception as e:
    conn.send(response('ERROR', str(e)))


# stream tensor
def tensor_stream(args, conn: Conn):
  tensor = Tensor.find(args[0])
  if not tensor: return
  
  iter = tensor.iter()
  ds   = DataStream(conn)

  while True:
    if not ds.write(iter.next()):
      break
    