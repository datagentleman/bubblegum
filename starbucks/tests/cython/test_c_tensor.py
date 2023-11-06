from starbucks.cython.tensor import CTensor as tensor

def test_c_tensor_open():
  ten = tensor()
  fd = ten.open(2, [b"datasets/iris/iris.csv"])

  print(fd)
  print(ten.print())