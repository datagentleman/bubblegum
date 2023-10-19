from __future__ import annotations

from typing import List
import os

# Main class for managing local datasets
class Dataset:
  PATH = "./datasets/"
  
  def __init__(self, name: str):
    self.name = name


  @staticmethod
  def ls() -> List[Dataset]:
    return [Dataset(name) for name in os.listdir(Dataset.PATH)]


  @classmethod
  def read(cls, name) -> bytes:
    f = open(f"{cls.PATH}/{name}", "rb")
    return f.read()  