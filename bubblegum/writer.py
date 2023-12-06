from struct import pack

class Writer:
  def __init__(self, data: bytes = b''): 
    self.data = bytearray(data)

  def write(self, val: any):
    match type(val).__name__:
      case 'int':
        self.data.extend(pack('i', val))
      
      case 'float':
        self.data.extend(pack('f', val))

      case 'str': 
        self.data.extend(self.data_with_size(val.encode()))

      case 'list' | 'tuple':
        self.write(len(val))
        [self.write(elem) for elem in val]

      case 'bytes':
        self.data.extend(self.data_with_size(val))

      case 'bytearray':
        self.data.extend(self.data_with_size(val))

      case _:
        print(f'writer - unknown type: {type(val).__name__}')

    return self


  def data_with_size(self, val: bytes) -> bytes:
    data_size = len(val).to_bytes(4, byteorder='little')
    return data_size + val
