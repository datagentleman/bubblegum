from configparser import ConfigParser

class _Config(type):
  def load(self, path: str):
    self.config = ConfigParser()
    self.config.read(path)


  def __getitem__(self, key):
    return self.config[key]
    

  def as_int(self, section, key):
    return self.config.getint(section, key)    


class Config(metaclass=_Config): 
  pass
