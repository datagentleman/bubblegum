from lib.buffer import Buffer
import numpy as np

def test_buffer():
  data = np.arange(20, dtype=np.int8).tobytes()
  buf = Buffer(data)
  
  assert(buf.data() == data)
  