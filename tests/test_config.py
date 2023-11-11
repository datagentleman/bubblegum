from starbucks.config import Config

def test_config_load():
  Config.load('test')

  assert(Config['server.host'] == 'localhost')
  assert(Config['server.port'] == 1337)
  