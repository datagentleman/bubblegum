from __future__ import annotations

from struct import pack

class Buffer:
  def __init__(self, packet =b''):
    self._data = packet


  # TODO: handle more types. Extract this logic.
  def write(self, data: any, num_of_bytes: int = 2, byteorder: str = 'little'):
    match type(data).__name__:
      case 'int':
        b = data.to_bytes(num_of_bytes, byteorder=byteorder)
        self._data += self.pack(b)

      case 'float':
        self._data += self.pack(pack('d', data))

      case 'str': 
        self._data += self.pack(data.encode())

      case 'list' | 'tuple':
        # write list len first
        self.write(len(data), 2)
        
        # write list itself
        for elem in data: self.write(elem)

      case 'bytes': 
        self._data += self.pack(data)

      case _:        
        self._data += self.pack(data)  

    return self


  def append(self, data: bytes):
    self._data += data


  # read next element
  def read(self) -> bytes:  
    # read size
    size = int.from_bytes(self._read(2), byteorder='little')
    
    # read data
    return self._read(size)
    
    
  def _read(self, len):
    bytes = self._data[:len]
    
    # we must delete consumed bytes after reading 
    self._data = self._data[len:]
    return bytes


  def pack(self, data: bytes) -> bytes:
    size = len(data).to_bytes(2, byteorder='little')
    return size + data
  

  def raw(self) -> bytes:
    return self.pack(self._data)

  
  def data(self) -> bytes:
    return self._data
  