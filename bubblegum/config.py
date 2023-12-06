from config import config

class _config(type):
  conf = config['dev']

  def load(self, env: str='dev'):
    self.conf = config[env]

  def __getitem__(self, key):
    return self.conf[key]


class Config(metaclass=_config): 
  pass
