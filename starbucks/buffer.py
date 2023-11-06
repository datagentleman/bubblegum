from __future__ import annotations

class Buffer:
  def __init__(self, packet=b''):
    self._data = packet


  def write(self, data: bytes):
    self._data += self.pack(data)
    return self


  def append(self, data: bytes):
    self._data += data


  # read next packet
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
  

  def pack(self, data) -> bytes:
    size = len(data).to_bytes(2, byteorder='little')
    return size + data
  

  def raw(self) -> bytes:
    return self.pack(self._data)

  
  def data(self) -> bytes:
    return self._data
  