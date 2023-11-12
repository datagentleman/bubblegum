import lib.tensor as tensor
import numpy as np


def test_tensor_open():
  t = tensor.Tensor().open(b'tensors/test.tensor')
  t.write(b'd')
  print(t.shape())

  dst = b''
  print(t.read(dst, 10))

  # ten = tensor()
  # ten.open(b'datasets/iris/iris.csv')
  
  # data = np.arange(10, dtype=np.int8).tobytes()

  # bytes_written = ten.write(data)
  # print(f'bytes written: {bytes_written}')
  # print(f'proper bytes: {data}')
  
  # data2 = ten.read(10) 
  # print(f"data: {data2}")

