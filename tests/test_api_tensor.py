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

  expect = {
    'name': 'test:llm', 'dtype': 'float16', 
    'shape': [0], 'fd': -1, 'max_bucket_size': 100000000 }

  assert(t.__dict__ == expect)

  # with given values
  res = c.tcreate('test:llm', "float32", [2, 2])
  assert(res.read('int') == status.OK)

  s, t = c.tload('test:llm')
  assert(s == status.OK)

  expect = {
    'name': 'test:llm', 'dtype': 'float32', 
    'shape': [2, 2], 'fd': -1, 'max_bucket_size': 100000000 }

  assert(t.__dict__ == expect)


@pytest.mark.api
def test_api_tsave_tload():
  c = Client(host, port).connect()

  res = c.tcreate('test:bert')
  assert(res.read('int') == status.OK)

  res = c.tsave('test:bert', 'float64', [255, 255, 255])
  assert(res == status.OK)
  
  s, t = c.tload('test:bert')
  assert(s == status.OK)

  expect = {
    'name': 'test:bert', 'dtype': 'float64', 
    'shape': [255, 255, 255], 'fd': -1, 'max_bucket_size': 100000000 }

  assert(t.__dict__ == expect)


@pytest.mark.api
def test_api_tremove():  
  c = Client(host, port).connect()

  res = c.tcreate('test:bert')
  assert(res.read('int') == status.OK)

  res = c.tremove('test:bert')
  assert(res.read('int') == status.OK)

  s, t = c.tload('test:bert')
  assert(s == status.ERR)
