import socket
from starbucks.packet import Message as msg
from starbucks.stream import Stream

def hello(args, stream: Stream):
  stream.send(b"Another latte?")
  