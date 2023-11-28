config = {
  "dev": {
    "server.host": "127.0.0.1",
    "server.port": 1337,
  },

  "test": {
    "server.host": "localhost",
    "server.port": 1337,
  }
}

class _Config(type):
  conf = config['dev']

  def load(self, env: str='dev'):
    self.conf = config[env]

  def __getitem__(self, key):
    return self.conf[key]


class Config(metaclass=_Config): 
  pass
