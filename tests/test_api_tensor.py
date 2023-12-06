import pytest

import bubblegum.status as status

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
  assert(res.read('int') == status.OK)

  s, t = c.tload('test:llm')
  assert(s == status.OK)
  
  expect = {'name': 'test:llm', 'dtype': 'float16', 'shape': [0], 'fd': -1, 'max_bucket_size': 100000000}
  assert(t.__dict__ == expect)
