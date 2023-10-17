from __future__ import annotations

class Buffer:
  def __init__(self, bytes=b''):
    self.data = bytearray()
    if len(bytes) > 0: self.write(bytes) 


  def write(self, data: bytes):
    size = len(data).to_bytes(2)
    self.data += size + data


  # read next packet
  def read(self) -> bytes:  
    # read data size
    raw  = self.data[:2]; del self.data[:2]
    size = int.from_bytes(raw, byteorder='big')
    
    # read data
    packet = self.data[:size]; del self.data[:size] 
    return bytes(packet)