import os
import traceback
import logging as log

from starbucks.node    import Node
from starbucks.api     import API
from starbucks.config  import Config  as config
from starbucks.command import Command as command

log.basicConfig(format="\x1b[6;37;44m%(levelname)s\x1b[0m:%(message)s", level=log.DEBUG)

HOST = config["server.host"]
PORT = config["server.port"]

command.COMMANDS = API

def handle_client(client_conn):
  while True:
    try:
      buf = client_conn.read()
      log.debug(f'Got data: {buf.data()}')

      command.run(command.from_bytes(buf), client_conn)
    except:
      log.error('Client is dead ...')
      break


if __name__ == '__main__':
  try:
    log.info(f'Starting starbucks node on host: {HOST} port: {PORT} pid: {os.getpid()}')
    Node(HOST, PORT).run(handle_client)
  except Exception as e:
    log.error(f'{traceback.format_exc()}')
