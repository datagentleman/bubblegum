import socket
from starbucks.packet import Message as msg

def hello(args, conn):
  msg.send(conn, b"Another latte?")
