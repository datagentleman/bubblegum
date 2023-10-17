from __future__ import annotations

import socket
from typing import Callable

from   starbucks.packet import Message, Message as msg
import starbucks.packet as packet 

class Command:
  COMMANDS = None
  
  def __init__(self, name, *args):
    self.name: str = name
    self.args: list[str] = args
    
    
  @classmethod
  def run(cls, cmd, conn):
    if not cmd.name in cls.COMMANDS:
      return conn.send(b"COMMAND DOESN'T EXIST!")

    cls.COMMANDS[cmd.name](cmd.args, conn)


  def to_bytes(self) -> bytearray:
    cmd   = packet.write_packet(self.name.encode())
    args  = [packet.write_packet(key.encode()) for key in self.args]
    count = packet.write_packet(len(args).to_bytes(2))

    return bytearray(cmd + count + b''.join(args))  


  @staticmethod
  def from_bytes(data: bytearray|bytes) -> Command:
    cmd = packet.read_packet(data).decode()
    
    # read number of arguments
    count = int.from_bytes(packet.read_packet(data), "big")
    args  = [packet.read_packet(data).decode() for _ in range(count)]
    
    return Command(cmd, *args)
  