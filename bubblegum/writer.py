from struct import pack, unpack

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
        buf = Writer()
        [buf.write(elem) for elem in val]
        
        # number of elements
        self.write(len(val))

        # number of bytes
        self.write(len(buf.data))

        self.data += buf.data
        
      case 'bytes':
        self.data.extend(self.data_with_size(val))

      case 'bytearray':
        self.data.extend(self.data_with_size(val))

      case _:
        print(f'writer - unknown type: {type(val).__name__}')

    return self


  def data_with_size(self, val: bytes) -> bytes:
    data_size = pack('<i', len(val))
    return data_size + val
