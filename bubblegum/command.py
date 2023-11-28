from __future__ import annotations

from typing import Any, Callable

from bubblegum.buffer import Buffer

class Command:
  def __init__(self, name: str, *args: tuple[Any, ...]):
    self.name = name
    self.args = args    
    self.handler: Callable = None


  def to_bytes(self) -> Buffer:
    buf = Buffer()
    buf.write(self.name)
    buf.write(self.args)
    return buf


  @classmethod
  def from_bytes(cls, buf: Buffer) -> Command:
    name = buf.read('str')

    # read and decode arguments
    args = buf.read('list', 'str')
    return Command(name, *args)
  