import traceback
import logging as log

from starbucks.server import Server
from starbucks.config import Config as config

log.basicConfig(format="\x1b[6;37;44m%(levelname)s\x1b[0m:%(message)s", level=log.DEBUG)
config.load('config.ini')

HOST = config["server"]["host"]
PORT = config.as_int("server", "port")

if __name__ == '__main__':
  try:
    log.info(f'Starting starbucks server on host: {HOST} port: {PORT}')
    Server(HOST, PORT).run() 
  except Exception as e:
    log.error(f'{traceback.format_exc()}')
