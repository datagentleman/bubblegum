from __future__ import annotations

class Buffer:
  def __init__(self, packet=b''):
    self.data = bytearray(packet)


  def write(self, data: bytes):
    self.data += self.pack(data)
    return self


  # read next packet
  def read(self) -> bytes:  
    # read data size
    raw  = self.data[:2]; del self.data[:2]
    size = int.from_bytes(raw, byteorder='big')
    
    # read data
    packet = self.data[:size]; del self.data[:size] 
    return bytes(packet)
  
  
  def pack(self, data) -> bytes:
    size = len(data).to_bytes(2)
    return size + data
    

  def raw(self) -> bytes:
    return self.pack(self.data)
  