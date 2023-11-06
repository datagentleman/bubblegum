from __future__ import annotations

from typing import Dict, Any, Callable

from starbucks.buffer import Buffer
from starbucks.stream import Stream

class Command:
  COMMANDS: Dict[str, Callable] = {}
  
  def __init__(self, name: str, *args):
    self.name: str = name
    self.args: tuple[Any, ...] = args    

    self.handler: Callable = None


  def run(self, stream: Stream):
    self.handler(self.args, stream)


  def to_bytes(self) -> Buffer:
    buf = Buffer()
    buf.write(self.name.encode())
    buf.write(len(self.args).to_bytes(2))
    
    [buf.write(key.encode()) for key in self.args]
    return buf

  @classmethod
  def from_bytes(cls, buf: Buffer) -> Command:
    name = buf.read().decode()

    # read arguments
    num = int.from_bytes(buf.read(), "big")
    args  = [buf.read().decode() for _ in range(num)]

    handler = cls.COMMANDS.get(name)
    if handler is None: 
      return None

    cmd = Command(name, *args)
    cmd.handler = handler

    return cmd
  