from starbucks.buffer import Buffer

def test_buffer_write_read():
  buf = Buffer()
  assert(buf.write(b'Hello').read('bytes') == b'Hello')

