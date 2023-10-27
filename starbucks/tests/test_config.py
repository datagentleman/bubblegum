from starbucks.config import Config

def test_config_load():
  Config.load('starbucks/tests/test_config.ini')
    
  assert(Config['server']['host'] == 'localhost')
  assert(Config.as_int('server', 'port') == 1337)
  