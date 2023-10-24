from __future__ import annotations

import os
import shutil

class Tensor:
  ROOT = "./tensors/"
  
  def __init__(self, name: str, dataset: str):
    self.name    = name
    self.dataset = dataset


  @classmethod
  def create(cls, path: str):
    os.makedirs(f'{cls.ROOT}/{path}', exist_ok=True)
  
  
  @classmethod
  def remove(cls, path: str):
    shutil.rmtree(f'{cls.ROOT}/{path}')
