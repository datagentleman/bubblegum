import pytest

from bubblegum.client import Client
from bubblegum.config import Config

Config.load('test')

@pytest.mark.api
def test_api_tcreate():
  c = Client(Config['server.host'], Config['server.port']).connect()
  res = c.tcreate('test:damianu_13')
  print(res.read('int'))
  