from __future__ import annotations

import os 
import shutil

from pathlib import Path
from starbucks.buffer import Buffer

class Tensor:
  ROOT = "./tensors/"
  TENSOR_INFO = "tensor.info"
    
  def __init__(self, name: str):
    self.name = name


  @classmethod
  def find(cls, path: str) -> Tensor|None:
    if Path(cls.ROOT).joinpath(path, cls.TENSOR_INFO).is_file():
      return Tensor(path)


  @classmethod
  def create(cls, path: str, root: str=ROOT):
    dir = Path(f'{root}/{path}')

    os.makedirs(dir, exist_ok=True)
    Path(f'{dir}/{cls.TENSOR_INFO}').touch()


  # TODO: remove only directories with tensor.info files.
  # Don't remove directory if there are sub-directories with other tensors. 
  @classmethod
  def remove(cls, path: str):
    shutil.rmtree(f'{cls.ROOT}/{path}')


  @classmethod
  def ls(cls, root: str=ROOT) -> list[tuple[str, ...]]:
    tensors = []

    # we only want directories with proper .data file inside
    for path in Path(root).rglob("*"):
      if path.joinpath(cls.TENSOR_INFO).is_file():
        tensors.append(path.parts[1:])
    
    return tensors
