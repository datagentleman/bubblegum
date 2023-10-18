from starbucks.buffer import Buffer

def test_buffer_write_read():
  assert(Buffer().write(b'Hello').read() == b'Hello')


def test_buffer_pack():
  assert(Buffer().pack(b'Hello') == b'\x00\x05Hello')

  
def test_buffer_raw():
  assert(Buffer().write(b'Hello').raw() == b'\x00\x07\x00\x05Hello')


