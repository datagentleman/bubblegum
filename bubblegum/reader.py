from struct import unpack

class Reader:
  def __init__(self, data: bytes = b''):
    self.data = bytearray(data)

  def read(self, type: str) -> any:
    if self.data == b'': return None

    types = self.parse_list(type)
    
    match types[0]:
      case "int":
        return unpack("i", self.read_length())[0]

      case "float":
        return unpack("f", self.read_length())[0]

      case "bytes":
        length = unpack('i', self.read_length())
        return self.read_length(length[0])

      case "str":
        length = unpack('i', self.read_length())
        return self.read_length(length[0]).decode()

      case "list":
        length = unpack('i', self.read_length())
        return [self.read(types[1]) for _ in range(length[0])]

      case _:
        print('unsupported type')


  def read_length(self, len=4):
    b = self.data[:len]
  
    # we must delete consumed bytes after reading 
    self.data[:] = self.data[len:]
    return b
    

  # This will parse something like 'list[int]' => ['list', 'int'] 
  def parse_list(self, type: str):
    return type.replace("[", " ").replace("]", "").split()