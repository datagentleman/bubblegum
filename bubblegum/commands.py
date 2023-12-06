from bubblegum.conn        import Conn
from bubblegum.buffer      import Buffer  
from bubblegum.tensor      import Tensor  

# TODO: add validation

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
