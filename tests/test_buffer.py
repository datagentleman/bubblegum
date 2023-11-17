from starbucks.buffer import Buffer

def test_buffer_write_read():
  buf = Buffer().write(b'Hello')
  assert(buf.read('bytes') == b'Hello')
  
  buf.write(1)
  assert(buf.read('int') == 1)

  buf.write(1.0001)
  assert(round(buf.read('float'), 4) == 1.0001)

  buf.write("bubblegum")
  assert(buf.read('string') == "bubblegum")

  buf.write(b'bubblegum')
  assert(buf.read('bytes') == b'bubblegum')
