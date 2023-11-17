from struct import pack
from typing import Any

class Writer:
  def write(self, data: any):
    match type(data).__name__:
      case 'int':
        return pack('i', data)
      
      case 'float':
        return pack('d', data)

      case 'str': 
        return self.write_len_data(data.encode())

      case 'list' | 'tuple':
        elems = b''.join([self.write(elem) for elem in data])
        
        data =  self.write(len(data))
        data += self.write(len(elems))
        data += elems

        return data
        
      case 'bytes': 
        return self.write_len_data(data)

      case _:        
        return self.write_len_data(data)  


  def write_len_data(self, data: bytes) -> bytes:
    size = len(data).to_bytes(4, byteorder='little')
    return size + data
