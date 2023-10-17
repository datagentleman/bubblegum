import socket
from starbucks.packet import Message, Message as msg

class Commands:
  @classmethod
  def handle_command(cls, conn: socket.socket, msg: Message):
    if not msg.cmd in cls.COMMANDS:
      return msg.send(conn, "COMMAND DOESN'T EXIST!")
    
    cls.COMMANDS[msg.cmd](cls, conn)
    
    
  def hello(cls, conn: socket.socket):
    msg.send(conn, "Another latte?")


  COMMANDS = {
    "HELLO": hello, 
  }
