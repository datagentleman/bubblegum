from __future__ import annotations

import socket
from starbucks.buffer import Buffer

class DataStream:
  def __init__(self, conn):
    self.conn = conn


  # writing bytes into stream.
  # write() should be called by server side.
  def write(self, data: bytes):
    buf = self.conn.read()
    cmd = buf.read()
    
    if cmd == b'NEXT':
      self.conn.send(Buffer().write(data))
      return True

    if cmd == b'END':
        return


  def next(self):
    self.conn.send(Buffer().write(b'NEXT'))
    res = self.conn.read()
    return res.data()


  def end(self):
    self.conn.send(Buffer().write(b'END'))


  # Peek next message in data stream
  def peek(self) -> bytes:
    # TODO: refactor this
    raw_msg = self.conn.conn.recv(1, socket.MSG_PEEK)
    
    return

    
  @classmethod
  def run(cls, client, path: str) -> DataStream:
    client.send('TSTREAM', path)
    return DataStream(client)
