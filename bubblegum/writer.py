from struct import pack

class Writer:
  def __init__(self, data: bytes = b''): 
    self.data = bytearray(data)

  def write(self, data: any): 
    match type(data).__name__:
      case 'int':
        self.data.extend(pack('i', data))
      
      case 'float':
        self.data.extend(pack('f', data))

      case 'str': 
        self.data.extend(self.data_with_size(data.encode()))

      case 'list' | 'tuple':
        self.write(len(data))
        [self.write(elem) for elem in data]

      case 'bytes':
        self.data.extend(self.data_with_size(data))

      case 'bytearray':
        self.data.extend(self.data_with_size(data))

      case _:
        print(f'unknown: {type(data).__name__}')
        pass

    return self

  def data_with_size(self, data: bytes) -> bytes:
    data_size = len(data).to_bytes(4, byteorder='little')
    return data_size + data
