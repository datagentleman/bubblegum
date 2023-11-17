from struct import unpack
from typing import Any

class Reader:
  def __init__(self, raw: bytes):
    self.data = raw


  def read(self, type_1: str, type_2: str=None, length: str="") -> any:
    format = length
    
    match type_1:
      case "int":
        format += "i"
        lst = unpack(format, self.read_length())
        return lst if len(lst) > 1 else lst[0]
        
      case "float":
        format += "f"
        lst = unpack(format, self.read_length())
        return lst if len(lst) > 1 else lst[0]
        
      case "bytes":
        length = unpack('i', self.read_length())[0]
        return self.read_length(length)

      case "string":
        length = unpack('i', self.read_length())[0]
        return self.read_length(length).decode()

      case "list":
        length = unpack('i', self.read_length())[0]
        return self.read(type_2, length=f'{length}')
        
      case _:
        print('unsupported type')


  def _read(self) -> bytes:
    # read size
    size = int.from_bytes(self.read_length(), byteorder='little')
    
    # read data
    return self.read_length(size)
      
      
  def read_length(self, len=4):
    b = self.data[:len]
    
    # we must delete consumed bytes after reading 
    self.data[:] = self.data[len:]
    return b
