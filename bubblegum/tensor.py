from __future__ import annotations

import os 
import shutil

from pathlib import Path
from struct  import pack, unpack

from bubblegum.buffer  import Buffer  

class Tensor:
  ROOT = "./tensors"
  EXT  = ".tensor"

  def __init__(self, name: str=None, dtype: str=None, shape: list(int)=None):
    self.name  = name or ""
    self.dtype = dtype or "float16"
    self.shape = shape or [0]
    self.fd    = -1

    # 100 MB
    self.max_bucket_size = 100_000_000


  def save(self):
    data = self.encode()
    size = pack('i', len(data))

    self.fd = self._open(self.name)
    os.pwrite(self.fd, size + data, 0)


  @classmethod
  def load(cls, name: str) -> Tensor:
    fd = cls._open(name)

    data = os.pread(fd, 4, 0)
    size = unpack('i', data)[0]

    data = os.pread(fd, size, 4)
    return cls.decode(data)


  # Encode tensor to bytes
  def encode(self) -> bytearray:
    buf = Buffer()

    buf.write(self.name)
    buf.write(self.dtype)
    buf.write(self.shape)
    return buf.data


  # Decode tensor from bytes
  @classmethod
  def decode(cls, data: bytes) -> Tensor:
    buf = Buffer(data)
    t = Tensor()

    t.name  = buf.read('str')
    t.dtype = buf.read('str')
    t.shape = buf.read('list[int]')
    return t


  @classmethod
  def _open(cls, name: str) -> int:
    fd = os.open(cls._path(name), os.O_RDWR | os.O_CREAT)
    return fd


  @classmethod
  def _path(cls, tensor: str):
    tensor = tensor.replace(":", "/")
    name = Path(tensor).name
    return Path(cls.ROOT).joinpath(tensor, f'{name}{cls.EXT}')


  @classmethod
  def _dir(cls, tensor: str):
    tensor = tensor.replace(":", "/")
    return Path(cls.ROOT).joinpath(tensor)


  # Find tensor
  @classmethod
  def find(cls, tensor: str) -> Tensor | None:
    if cls._path(tensor).is_file():
      return Tensor(tensor)
      

  # Create tensor directories and necessary files
  @classmethod
  def create(cls, name: str, dtype: str=None, shape: list(int)=None):
    os.makedirs(cls._dir(name), exist_ok=True)
    Path(cls._path(name)).touch(exist_ok=True)

    Tensor(name, dtype, shape).save()


  @classmethod
  def remove(cls, tensor: str, root: str=ROOT, force: bool=False):
    # remove whole directory including sub-directories
    if force: shutil.rmtree(cls._dir(tensor))
      
    # TODO: just remove all files from dir
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


  # List all tensors 
  @classmethod
  def ls(cls, root: str=ROOT) -> list[tuple[str, ...]]:
    tensors = []

    # We only want directories with .tensor file
    for path in Path(root).rglob("*"):
      if path.is_file() and path.suffixes[0] == cls.EXT:
        tensors.append(path.parts[1:-1])

    return tensors
