import pytest

from bubblegum.client import Client
from bubblegum.config import Config

Config.load('test')

host = Config['server.host']
port = Config['server.port']

@pytest.mark.api
def test_api_tcreate():
  c = Client(host, port).connect()

  # with default values
  res = c.tcreate('test:llm')
  assert(res.read('int') == 1)
  