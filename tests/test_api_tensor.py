import pytest
import numpy as np
import bubblegum.status as status

from timeit           import default_timer as timer
from bubblegum.client import Client
from bubblegum.config import Config

Config.load('test')

host = Config['server.host']
port = Config['server.port']

@pytest.mark.api
def test_api_tput():  
  c = Client(host, port).connect()
  data = np.arange(100000000, dtype=np.int32).tobytes()

  start = timer()
  s = c.tcreate('test:llm')
  assert(s == status.OK)

  s = c.tput("test:llm", data)
  assert(s == status.OK)

  end = timer()
  print(f'Elapsed time 2: {(end-start)}')

@pytest.mark.api
def test_api_tget():  
  c = Client(host, port).connect()
  data = np.arange(1000000, dtype=np.int32).tobytes()

  s = c.tcreate('test:llm', "int32")
  assert(s == status.OK)

  s = c.tput("test:llm", data)
  assert(s == status.OK)
  
  c = Client(host, port).connect()
  s = c.tget("test:llm", 10)


@pytest.mark.api
def test_api_tcreate():
  c = Client(host, port).connect()

  # with default values
  s = c.tcreate('test:llm')
  assert(s == status.OK)

  s, t = c.tload('test:llm')
  assert(s == status.OK)

  expect = {
    'name': 'test:llm', 'dtype': 'float16', 
    'shape': [0], 'fd': -1, 'max_bucket_size': 100000000 }

  assert(t.__dict__ == expect)

  # with given values
  s = c.tcreate('test:llm', "float32", [2, 2])
  assert(s == status.OK)

  s, t = c.tload('test:llm')
  assert(s == status.OK)

  expect = {
    'name': 'test:llm', 'dtype': 'float32', 
    'shape': [2, 2], 'fd': -1, 'max_bucket_size': 100000000 }

  assert(t.__dict__ == expect)


@pytest.mark.api
def test_api_tsave_tload():
  c = Client(host, port).connect()

  s = c.tcreate('test:bert')
  assert(s == status.OK)

  s = c.tsave('test:bert', 'float64', [255, 255, 255])
  assert(s == status.OK)
  
  s, t = c.tload('test:bert')
  assert(s == status.OK)

  expect = {
    'name': 'test:bert', 'dtype': 'float64', 
    'shape': [255, 255, 255], 'fd': -1, 'max_bucket_size': 100000000 }

  assert(t.__dict__ == expect)


@pytest.mark.api
def test_api_tremove():  
  c = Client(host, port).connect()

  s = c.tcreate('test:bert')
  assert(s == status.OK)

  s = c.tremove('test:bert')
  assert(s == status.OK)

  s, _ = c.tload('test:bert')
  assert(s == status.ERR)



