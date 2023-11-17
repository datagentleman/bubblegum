from struct import unpack

class Reader:
  def __init__(self, raw: bytes):
    self.data = raw

  def read(self, type_1: str, type_2: str=None, length: str="") -> any:
    format = length
    
    match type_1:
      case "int":
        format += "i"
        return unpack(format, self._read())
        
      case "bytes":
        len = unpack('i', self.read_length())[0]
        return self.read_length(len)

      case "list":
        len = unpack('i', self.read_length())
        return self.read(type_2, length=f'{len[0]}')
        
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
    self.data = self.data[len:]
    return b
