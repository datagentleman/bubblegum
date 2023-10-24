import os
from starbucks.tensor import Tensor

def test_tensor_create_remove():
  path = 'iris/validation/w1'
  Tensor.create(path)
  assert(os.path.exists(Tensor.ROOT + path))
  
  Tensor.remove(path)
  assert not(os.path.exists(Tensor.ROOT + path))