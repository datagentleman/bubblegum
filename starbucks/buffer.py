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
    raw = self._data[:2]
    self._data = self._data[2:]
    
    size = int.from_bytes(raw, byteorder='big')
    
    # read data
    packet = self._data[:size]
    self._data = self._data[size:] 
    
    return packet
  
  
  def pack(self, data) -> bytes:
    size = len(data).to_bytes(2)
    return size + data
    

  def raw(self) -> bytes:
    return self.pack(self._data)

  
  def data(self) -> bytes:
    return self._data
