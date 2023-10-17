from __future__ import annotations

from starbucks.buffer import Buffer
from starbucks.packet import Message as msg

class Command:
  COMMANDS = None
  
  def __init__(self, name, *args):
    self.name: str = name
    self.args: list[str] = args
    
    
  @classmethod
  def run(cls, cmd, conn):
    if not cmd.name in cls.COMMANDS:
      return msg.send(conn, b"COMMAND DOESN'T EXIST!")
  
    cls.COMMANDS[cmd.name](cmd.args, conn)


  def to_bytes(self) -> Buffer:
    buf = Buffer()
    buf.write(self.name.encode())
    buf.write(len(self.args).to_bytes(2))
    
    [buf.write(key.encode()) for key in self.args]
    
    return buf


  @staticmethod
  def from_bytes(buf: Buffer) -> Command:
    cmd = buf.read().decode()
    
    # read number of arguments
    count = int.from_bytes(buf.read(), "big")
    args  = [buf.read().decode() for _ in range(count)]
    
    return Command(cmd, *args)
  