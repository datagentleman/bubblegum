from config import config

class _Config(type):
  conf = config['dev']

  def load(self, env: str='dev'):
    self.conf = config[env]

  def __getitem__(self, key):
    return self.conf[key]


class Config(metaclass=_Config): 
  pass
