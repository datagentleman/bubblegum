from lib.buffer import Buffer
import numpy as np

def test_c_buffer():
  data = np.arange(20, dtype=np.int8).tobytes()
  buf = Buffer(data)
  
  print(buf.data() == data)