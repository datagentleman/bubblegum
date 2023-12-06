import lib.tensor as tensor
import numpy as np

def test_tensor_save():
  t1 = tensor.Tensor(b'tensors/test_load.tensor')
  t1.shape = [1, 2, 3]
  t1.dtype = "int16".encode()
  t1.save()

  t2 = tensor.Tensor(b'tensors/test_load.tensor')
  t2.load()

  assert(t1.shape == t2.shape)
  assert(t1.dtype == t2.dtype)
  
