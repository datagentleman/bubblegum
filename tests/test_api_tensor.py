import pytest
import numpy as np
from timeit import default_timer as timer

import bubblegum.status as status
import bubblegum.client as bubblegum

from bubblegum.config import Config

Config.load('test')

host = Config['server.host']
port = Config['server.port']

@pytest.mark.api
def test_api_tput():  
  c = bubblegum.connect(host, port)

  data = np.arange(10000000, dtype=np.int32).tobytes()

  start = timer()
  t = c.tensor('test:llama')
  assert(t)

  s = t.put(data)
  assert(s == status.OK)

  end = timer()
  print(f'Elapsed time 2: {(end-start)}')


@pytest.mark.api
def test_api_tget():  
  c = bubblegum.connect(host, port)
  data = np.arange(100000000, dtype=np.int32).tobytes()

  t = c.tensor('test:llm', "int32", [2, 2])
  assert(t)

  s = t.save('int32', [2, 2])
  assert(s == status.OK)

  t = c.tensor('test:llm')
  s = t.put(data)
  assert(s == status.OK)

  t = bubblegum.connect(host, port).tensor('test:llm')
  s, rows = t.get(10)
  
  assert(s == status.OK)
  assert(rows == data[:160])


@pytest.mark.api
def test_api_tset():
  c = bubblegum.connect(host, port)
  old_data = np.arange(1000000, dtype=np.int32).tobytes()

  t = c.tensor("test:llm", "int32", [2, 2])
  assert(t)

  s = t.put(old_data)
  assert(s == status.OK)

  c = bubblegum.connect(host, port)
  new_data = np.random.randint(10, size=1000000, dtype=np.int32).tobytes()

  t = c.tensor("test:llm")
  s = t.set(new_data)
  assert(s == status.OK)

  c = bubblegum.connect(host, port)
  t = c.tensor("test:llm")
  s, rows = t.get(1000000)

  assert(s == status.OK)
  assert(rows == new_data)


@pytest.mark.api
def test_api_tcreate():
  c = bubblegum.connect(host, port)

  # with default values
  t = c.tcreate('test:llm')
  assert(t)

  t = c.tload('test:llm')
  assert(t)

  expect = {'name': 'test/llm', 'dtype': 'float16', 'shape': [0]}
  assert(t.__repr__() == expect)

  # with given values
  t = c.tcreate('test:llm', "float32", [2, 2])
  assert(t)

  t = c.tload('test:llm')
  assert(t)

  expect = {'name': 'test/llm', 'dtype': 'float32', 'shape': [2, 2]}
  assert(t.__repr__() == expect)


@pytest.mark.api
def test_api_tsave_tload():
  c = bubblegum.connect(host, port)

  s = c.tcreate('test:bert')
  assert(s == status.OK)

  t = c.tensor("test:bert")
  s = t.save('float32', [255, 255, 255])
  assert(s == status.OK)
  
  s, t = c.tload('test:bert')
  assert(s == status.OK)

  expect = {'name': 'test/bert', 'dtype': 'float32', 'shape': [255, 255, 255]}
  assert(t.__repr__() == expect)

@pytest.mark.api
def test_api_tremove():  
  c = bubblegum.connect(host, port)

  s = c.tcreate('test:bert')
  assert(s == status.OK)

  s = c.tremove('test:bert')
  assert(s == status.OK)

  s, _ = c.tload('test:bert')
  assert(s == status.ERR)



