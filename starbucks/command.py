from __future__ import annotations

from typing import Dict, Any, Callable

from starbucks.buffer import Buffer
from starbucks.stream import Stream

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
    name = buf.read().decode()

    # read and decode arguments
    num  = int.from_bytes(buf.read(), "little")
    args = [buf.read().decode() for _ in range(num)]

    return Command(name, *args)
  