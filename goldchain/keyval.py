from __future__ import annotations
from fileutils  import open_path

ROOT_DIR = conf['ROOT_DIR']


class KeyVal:
  def __init__(self, name: str, file: File):
    self.fd = fd


  # def read_header(self):
  #   self.header.encode_data(read_bytes(self.file))
  #   decode_data(self.header, read_bytes(self.file))
  def write_header(self):
    write(encode(self.header), self.file, 0)


# Opens or creates keyval collection.
def open(name: str) -> KeyVal:
  file = open_path(f"{ROOT_DIR}/kv/{name}/{name}.kv")

  file = file()
  buf  = buffer(bytes)

  # read(self.age,  buf)
  # read(self.name, buf)

  # write(self.age,  buf)
  # write(self.name, buf)
  
  # bytes = bytearray()

  return KeyVal(name, file)
