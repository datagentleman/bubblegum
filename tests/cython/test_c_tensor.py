import lib.tensor as tensor
import numpy as np
def test_tensor_save():
  t = tensor.Tensor().open(b'tensors/test_load.tensor')
  data = np.arange(2, dtype=np.int32).tobytes()

  t.shape = [1, 8, 5, 12, 8]
  t.save()
  t.load()
