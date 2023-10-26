from __future__ import annotations

import os 
import shutil

from pathlib import Path
from starbucks.buffer import Buffer

class Tensor:
  ROOT = "./tensors/"
  
  def __init__(self, name: str, dataset: str):
    self.name    = name
    self.dataset = dataset


  @classmethod
  def create(cls, path: str, root: str=ROOT):
    dir = Path(f'{root}/{path}')

    os.makedirs(dir, exist_ok=True)
    Path(f'{dir}/{dir.name}.data').touch()


  # TODO: remove only directories with .data files.
  # Don't remove directory if there are sub-directories with other tensors. 
  @classmethod
  def remove(cls, path: str):
    shutil.rmtree(f'{cls.ROOT}/{path}')


  @classmethod
  def ls(cls, root: str=ROOT) -> list[tuple[str, ...]]:
    tensors = []

    # we only want directories with proper .data file inside
    for path in Path(root).rglob("*"):
      if path.joinpath(path.name + ".data").is_file():
        tensors.append(path.parts[1:])
    
    return tensors
