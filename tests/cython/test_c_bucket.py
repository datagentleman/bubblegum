from lib.bucket import Bucket
import numpy as np

def test_bucket_write():
  data = np.arange(2, dtype=np.int32).tobytes()

  b = Bucket(b'tensors/iris/1.bucket')
  b.write(data)

  buf = b.read(2)
  assert(data == buf)
