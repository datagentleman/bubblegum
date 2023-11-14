from struct  import pack, unpack
import numpy as np

from lib.buffer import Buffer

def test_buffer_write():
  buf = Buffer()
  
  raw1 = pack("HHH", 1, 2, 3)
  raw2 = pack("bbb", 4, 5, 6)
  raw3 = pack("HHH", 7, 8, 9)
  
  buf.write(raw1)
  buf.write(raw2)
  buf.write(raw3)

  raw = bytearray(6)
  buf.read(raw)
  assert(raw == raw1)
  
  raw = bytearray(3)
  buf.read(raw)
  assert(raw == raw2)

  raw = bytearray(6)
  buf.read(raw)
  assert(raw == raw3)
