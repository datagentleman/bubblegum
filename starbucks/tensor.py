from __future__ import annotations

import os 
import shutil

from pathlib import Path
from starbucks.dataset import Dataset  

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
    self.name = name


  def iter(self) -> TensorIterator:
    return TensorIterator(self)


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
    if force: shutil.rmtree(cls._dir(tensor))
      
    for file in cls._dir(tensor).glob('*.tensor'):
      os.remove(file)

    for file in cls._dir(tensor).glob('*.bucket'):
      os.remove(file)
    
    # This will remove dir only if it's empty. If not then we will get exception
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
