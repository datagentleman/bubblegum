from __future__ import annotations

import os 
import shutil

from pathlib import Path

from starbucks.dataset import Dataset  
from starbucks.buffer  import Buffer  

class TensorIterator:
  def __init__(self, tensor: Tensor):
    self.tensor = tensor
    
  def next(self) -> bytes:
    # POC: only temporary
    return Dataset.read('iris/iris.csv')


class Tensor:
  ROOT = "./tensors"
  EXT  = ".tensor"
  
  def __init__(self, name: str):
    self.name  = name
    self.dtype = ""
    self.shape = ()
    self.rows_per_bucket  = 10_000
    self.buckets_per_node = 0


  def iter(self) -> TensorIterator:
    return TensorIterator(self)


  # Encode tensor to bytes
  def bytes(self) -> bytearray:
    buf = Buffer()
    
    buf.write(self.name)
    buf.write(self.dtype)
    buf.write(self.shape)
    buf.write(self.rows_per_bucket)
    buf.write(self.buckets_per_node)
    
    return buf.data


  # Decode tensor from bytes
  @classmethod
  def from_bytes(cls, data: bytes) -> Tensor:
    buf = Buffer(data)
    t = Tensor("")
    
    t.name  = buf.read('str')
    t.dtype = buf.read('str')
    t.shape = buf.read('list', 'int')
    
    t.rows_per_bucket  = buf.read('int')
    t.buckets_per_node = buf.read('int')
    
    return t
    

  @classmethod
  def _path(cls, tensor: str):
    name = Path(tensor).name
    return Path(cls.ROOT).joinpath(tensor, f'{name}{cls.EXT}')


  @classmethod
  def _dir(cls, tensor: str):
    return Path(cls.ROOT).joinpath(tensor)
    

  @classmethod
  def find(cls, tensor: str) -> Tensor:
    if cls._path(tensor).is_file():
      return Tensor(tensor)


  @classmethod
  def create(cls, tensor: str, root: str=ROOT):
    os.makedirs(cls._dir(tensor), exist_ok=True)
    Path(cls._path(tensor)).touch()


  @classmethod
  def remove(cls, tensor: str, root: str=ROOT, force: bool=False):
    # remove whole directory including sub-directories
    if force: shutil.rmtree(cls._dir(tensor))
      
    for file in cls._dir(tensor).glob('*.tensor'):
      os.remove(file)

    for file in cls._dir(tensor).glob('*.bucket'):
      os.remove(file)
    
    # This will remove dir only if it's empty. If not empty, we will get exception
    # which we can ignore. 
    try:
      cls._dir(tensor).rmdir()
    except Exception:
      pass


  @classmethod
  def ls(cls, root: str=ROOT) -> list[tuple[str, ...]]:
    tensors = []

    # We only want directories with proper .tensor file
    for path in Path(root).rglob("*"):
      if path.is_file() and path.suffixes[0] == cls.EXT:
        tensors.append(path.parts[1:-1])
    
    return tensors
