from __future__ import annotations
from starbucks.buffer import Buffer

class DataStream:
  def __init__(self, conn):
    self.conn = conn


  # write() should be called by server
  def write(self, data: bytes):
    buf = self.conn.read()
    cmd = buf.read()
    
    if cmd == b'NEXT':
      self.conn.send(Buffer().write(data))
      return True

    if cmd == b'END':
        return


  def next(self):
    self.conn.stream.send(Buffer().write(b'NEXT'))
    res = self.conn.read()
    return res.data()


  def end(self):
    self.conn.stream.send(Buffer().write(b'END'))

    
  @classmethod
  def run(cls, client, path: str) -> DataStream:
    client.send('TSTREAM', path)
    return DataStream(client)
