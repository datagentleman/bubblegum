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
