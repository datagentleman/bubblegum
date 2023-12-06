from bubblegum.buffer import Buffer

def test_reader():
  buf = Buffer()

  buf.write((1, 2, 3))
  assert(buf.read('list[int]') == [1, 2, 3])

  
  