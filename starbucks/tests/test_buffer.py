from starbucks.buffer import Buffer

def test_buffer_write_read():
  buf = Buffer()
  assert(buf.write(b'Hello').read() == b'Hello')


def test_buffer_pack():
  buf = Buffer()
  assert(buf.pack(b'Hello') == b'\x00\x05Hello')

  
def test_buffer_raw():
  buf = Buffer()
  assert(buf.write(b'Hello').raw() == b'\x00\x07\x00\x05Hello')


