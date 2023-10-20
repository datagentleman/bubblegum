from __future__ import annotations

from starbucks.buffer import Buffer
from starbucks.stream import Stream

class Command:
  COMMANDS = {}
  
  def __init__(self, name, *args):
    self.name: str = name
    self.args: list[str] = args
    
    
  @classmethod
  def run(cls, cmd, stream: Stream):
    handler = cls.COMMANDS.get(cmd.name)
    
    if handler is None: 
      return stream.send(b"COMMAND DOESN'T EXIST!")
    
    handler(cmd.args, stream)


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
  