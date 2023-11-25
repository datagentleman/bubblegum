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


  # TODO: remove only .tensor file and all .bucket files. If dir became empty, also remove it.
  @classmethod
  def remove(cls, tensor: str):
    shutil.rmtree(cls._dir(tensor))


  @classmethod
  def ls(cls, root: str=ROOT) -> list[tuple[str, ...]]:
    tensors = []

    # we only want directories with proper .tensor file
    for path in Path(root).rglob("*"):
      if path.is_file() and path.suffixes[0] == cls.EXT:
        tensors.append(path.parts[1:-1])
    
    return tensors
