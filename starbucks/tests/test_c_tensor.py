from starbucks.ctensor import CTensor as tensor

def test_c_tensor_open():
  assert(tensor().hello() == b'hello world')