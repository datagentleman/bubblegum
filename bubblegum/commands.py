from bubblegum.conn        import Conn
from bubblegum.buffer      import Buffer  
from bubblegum.tensor      import Tensor  

# TODO: add validations

# Create tensor
def tcreate(cmd: Buffer):
  name  = cmd.read('str')
  dtype = cmd.read('str')
  shape = cmd.read('list[int]')
  Tensor.create(name, dtype, shape)


# Load tensor from file
def tload(cmd: Buffer) -> bytes:
  name = cmd.read('str')
  return Tensor.load(name).encode()


# Save tensor to file. This will overwrite previous data. 
def tsave(cmd: Buffer):
  t = Tensor()

  t.name  = cmd.read('str')
  t.dtype = cmd.read('str')
  t.shape = cmd.read('list[int]')
  t.save()