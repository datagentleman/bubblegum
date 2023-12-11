import os
import traceback
import logging as log

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
  cmd_name = conn.read()

  # Conn is consider closed when it's ready for read but there is no data. 
  # We can unregister it from select loop and return.
  if len(cmd_name.data) == 0:
    print(f'UNREGISTER CLIENT: {conn.fileno()}')
    node.select.unregister(conn)
    return

  res = None

  response_ok  = lambda data=None: conn.send(buffer.write(status.OK, data))
  response_err = lambda data=None: conn.send(buffer.write(status.ERR, data))

  try:
    match cmd_name.read('str'):
      case "TPUT":
        node.select.unregister(conn)
        c_commands.t_put(conn.fileno())

      case "TGET": 
        node.select.unregister(conn)
        c_commands.t_get(conn.fileno())

      case "TCREATE": 
        args = conn.read(); 
        res  = tcreate(args)
        response_ok(res)

      case "TREMOVE": 
        args = conn.read(); 
        res = tremove(args)
        response_ok(res)

      case "TLOAD":   
        args = conn.read(); 
        res = tload(args)
        response_ok(res)

      case "TSAVE":   
        args = conn.read(); 
        res = tsave(args)
        response_ok(res)

      case _: 
        response_err(b"COMMAND DOESN'T EXIST")

  except Exception as e:
    log.error(f'{traceback.format_exc()}')
    response_err()


if __name__ == '__main__':
  try:
    log.info(f'Starting bubblegum node on host: {HOST} port: {PORT} pid: {os.getpid()}')
    Node(HOST, PORT).run(run_command)
  except Exception as e:
    log.error(f'{traceback.format_exc()}')
