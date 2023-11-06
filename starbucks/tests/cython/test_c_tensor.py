from starbucks.cython.tensor import CTensor as tensor
import numpy as np

def test_c_tensor_open():
  ten = tensor()
  ten.open(b'datasets/iris/iris.csv')

  data = np.arange(10).tobytes()
  print(data)
  print(f'LEN: {len(data)}')

  bytes_written = ten.write(data)
  print(f'bytes written: {bytes_written}')
  