import os
from starbucks.tensor import Tensor

def test_tensor_create_remove():
  path = 'iris/validation/w1'

  Tensor.create(path)
  assert(os.path.exists(Tensor.ROOT + path))
  
  Tensor.remove(path)
  assert not(os.path.exists(Tensor.ROOT + path))
  

def test_tensor_ls():
  Tensor.remove("iris")
  Tensor.create("iris/validation/w1")
  
  tensors = Tensor.ls()
  
  assert(len(tensors) == 1)
  assert(tensors[0] == ('iris', 'validation', 'w1'))