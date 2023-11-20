from struct import pack

class Writer:
  def __init__(self, data: bytearray): 
    self.data = data

  def write(self, data: any): 
    match type(data).__name__:
      case 'int':
        self.data.extend(pack('i', data))
      
      case 'float':
        self.data.extend(pack('f', data))

      case 'str': 
        self.data.extend(self.write_len_data(data.encode()))

      case 'list' | 'tuple':
        self.write(len(data))
        [self.write(elem) for elem in data]
        
      case 'bytes': 
        self.data.extend(self.write_len_data(data))

      case _:
        self.data.extend(self.write_len_data(data))
        

  def write_len_data(self, data: bytes) -> bytes:
    size = len(data).to_bytes(4, byteorder='little')
    return size + data
