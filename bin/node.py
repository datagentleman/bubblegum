import os
import traceback
import logging as log

from enum import Enum

from bubblegum.conn     import Conn
from bubblegum.node     import Node
from bubblegum.config   import Config 
from bubblegum.commands import * 

import bubblegum.status as status  
import bubblegum.buffer as buffer 
import lib.commands     as c_commands

log.basicConfig(format="\x1b[6;37;44m%(levelname)s\x1b[0m:%(message)s", level=log.DEBUG)

HOST = Config["server.host"]
PORT = Config["server.port"]

def run_command(conn: Conn, node: Node):
  msg = conn.read()
  
  # Conn is consider closed when it's ready for read but there is no data. 
  # We can unregister it from select loop and return.
  if len(msg.data) == 0: 
    node.select.unregister(conn)
    return

  cmd = msg.read('str')

  response_ok  = lambda data=None: conn.send(buffer.write(status.OK))
  response_err = lambda data=None: conn.send(buffer.write(status.ERR))

  match cmd:
    case "TCREATE":
      tcreate(msg)
      response_ok()

    case _:
      conn.send(b"COMMAND DOESN'T EXIST")
      raise TypeError()


if __name__ == '__main__':
  try:
    log.info(f'Starting bubblegum node on host: {HOST} port: {PORT} pid: {os.getpid()}')
    Node(HOST, PORT).run(run_command)
  except Exception as e:
    log.error(f'{traceback.format_exc()}')
