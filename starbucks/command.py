from __future__ import annotations

from typing import Dict, Any, Callable

from starbucks.buffer import Buffer
from starbucks.stream import Stream

class Command:
  COMMANDS: Dict[str, Callable] = {}
  
  def __init__(self, name: str, *args):
    self.name: str = name
    self.args: tuple[Any, ...] = args
    
    
  @classmethod
  def run(cls, cmd, stream: Stream):
    cmd_handler = cls.COMMANDS.get(cmd.name)

    if cmd_handler is None: 
      return stream.send(Buffer(b"COMMAND DOESN'T EXIST!"))
    
    cmd_handler(cmd.args, stream)


  def to_bytes(self) -> Buffer:
    buf = Buffer()
    buf.write(self.name.encode())
    buf.write(len(self.args).to_bytes(2))
    
    [buf.write(key.encode()) for key in self.args]
    return buf


  @staticmethod
  def from_bytes(buf: Buffer) -> Command:
    name = buf.read().decode()

    # read number of arguments
    raw_size = buf.read()
    count = int.from_bytes(raw_size, "big")
    args  = [buf.read().decode() for _ in range(count)]
    
    return Command(name, *args)
  