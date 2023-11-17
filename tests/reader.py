from starbucks.buffer import Buffer
from starbucks.reader import reader

def test_reader():
  buf = Buffer()

  data = buf.write((1, 2, 3))
  buf._data = data

  assert(reader(buf, "list", "int") == (1, 2, 3))

  
  