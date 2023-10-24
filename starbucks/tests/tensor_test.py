import os
from starbucks.tensor import Tensor

def test_tensor_create():
  path = 'iris/validation/w1'
  Tensor.create(path)
  assert(os.path.exists(Tensor.ROOT + path))