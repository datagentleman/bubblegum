from __future__ import annotations

import os
import shutil

from pathlib import Path

class Tensor:
  ROOT = "./tensors/"
  
  def __init__(self, name: str, dataset: str):
    self.name    = name
    self.dataset = dataset


  @classmethod
  def create(cls, path: str, root: str=ROOT):
    dir = Path(f'{root}/{path}')
    os.makedirs(dir, exist_ok=True)
       
    tensor = os.path.basename(dir)
    Path(f'{dir}/{tensor}.data').touch()

  
  # TODO: remove only directories with .data files.
  # Don't remove directory if there are sub-directories with other tensors. 
  @classmethod
  def remove(cls, path: str):
    shutil.rmtree(f'{cls.ROOT}/{path}')


  @classmethod
  def ls(cls, root: str=ROOT) -> list[tuple[str, ...]]:
    tensors = []
    
    # we only want directories with proper basename.data file inside
    for path in Path(root).rglob("*"):
       if path.is_dir():
          data_file = f'{path}/{path.name}.data'
          
          if os.path.exists(data_file):
            tensors.append(path.parts[1:])

    return tensors
