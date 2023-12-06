import os
from bubblegum.tensor import Tensor
from pathlib import Path

def test_tensor_create_remove():
  path = 'test/iris/validation/w1'

  Tensor.create(path)
  assert(os.path.exists(Path(Tensor.ROOT).joinpath(path)))
  
  Tensor.remove(path)
  assert not(os.path.exists(Path(Tensor.ROOT).joinpath(path)))

  # When we have nested tensors, we don't want to remove directories
  path1 = 'test/iris/validation/w1'
  path2 = 'test/iris/validation/w1/w2'

  Tensor.create(path1)
  Tensor.create(path2)

  Tensor.remove(path1)
  assert(os.path.exists(Path(Tensor.ROOT).joinpath(path1)))
  assert(os.path.exists(Path(Tensor.ROOT).joinpath(path2)))
  
  
def test_tensor_ls():
  Tensor.remove("test", force=True)
  Tensor.create("test/iris/validation/w1")
  
  tensors = Tensor.ls('tensors/test')
  
  assert(len(tensors) == 1)
  assert(tensors[0] == ('test', 'iris', 'validation', 'w1'))


def test_find():
  Tensor.remove("test", force=True)
  Tensor.create("test/iris")
  
  tensor = Tensor.find("test/iris")
  assert(isinstance(tensor, Tensor))
  
  tensor = Tensor.find("test/fake")
  assert(tensor == None)


def test_from_to_bytes():
  t1 = Tensor("test/iris")
  t1.dtype = "int16"
  t1.shape = [2, 3]
  
  t2 = Tensor.decode(t1.encode())
  assert(t1.encode() == t2.encode())


def test_save_load():
  path = 'test/iris/validation/w1'
  Tensor.create(path)
  
  t1 = Tensor(path)
  t1.dtype = "int32"
  t1.shape = [2, 3]
  t1.save()
  
  t2 = Tensor.load(path)
  assert(t1.encode() == t2.encode())
