from bubblegum.connection  import Connection as Conn
from bubblegum.buffer      import Buffer  
from bubblegum.tensor      import Tensor  

import datetime

# TODO: add validations

# Create tensor
def tcreate(cmd: Buffer):
  start = datetime.datetime.now()

  name  = cmd.read('str')
  dtype = cmd.read('str')
  shape = cmd.read('list[int]')
  Tensor.create(name, dtype, shape)
  
  end = datetime.datetime.now()
  print(f'Elapsed time 2: {(end-start).microseconds/1000000}')


# Remove tensor files and directory (if possible)
def tremove(cmd: Buffer):
  name = cmd.read('str')
  Tensor.remove(name)


# Load tensor from file
def tload(cmd: Buffer) -> bytes:
  name = cmd.read('str')

  if not Tensor.find(name): raise TypeError(f'Tensor {name} not found')
  return Tensor.load(name).encode()


# Save tensor to file. This will overwrite previous data. 
def tsave(cmd: Buffer):
  t = Tensor()

  t.name  = cmd.read('str')
  t.dtype = cmd.read('str')
  t.shape = cmd.read('list[int]')
  t.save()
  