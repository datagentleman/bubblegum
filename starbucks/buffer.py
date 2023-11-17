from __future__ import annotations

from struct import pack

class Buffer:
  def __init__(self, packet = b''):
    self._data = packet

  # TODO: handle more types. Extract this logic.
  def write(self, data: any):
    match type(data).__name__:
      case 'int':
        return pack('i', data)
      
      case 'float':
        return pack('d', data)

      case 'str': 
        return self.pack(data.encode())

      case 'list' | 'tuple':
        elems = b''.join([self.write(elem) for elem in data])
        
        data =  self.write(len(data))
        data += self.write(len(elems))
        data += elems

        return data
        
      case 'bytes': 
        return self.pack(data)

      case _:        
        return self.pack(data)  


  def append(self, data: bytes):
    self._data += data


  # read next 
  def read(self) -> bytes:  
    # read size
    size = int.from_bytes(self._read(4), byteorder='little')
    
    # read data
    return self._read(size)
    
    
  def read_length(self):
    bytes = self._data[:4]
    
    # we must delete consumed bytes after reading 
    self._data = self._data[4:]
    return bytes
    
    
  def _read(self, len):
    bytes = self._data[:len]
    
    # we must delete consumed bytes after reading 
    self._data = self._data[len:]
    return bytes


  def pack(self, data: bytes) -> bytes:
    size = len(data).to_bytes(4, byteorder='little')
    return size + data
  

  def raw(self) -> bytes:
    return self.pack(self._data)

  
  def data(self) -> bytes:
    return self._data
