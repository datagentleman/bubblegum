from struct import unpack
from starbucks.buffer import Buffer

def reader(buff: Buffer, type_1: str, type_2: str=None, length: str="") -> any:
  format = length
  
  match type_1:
    case "int":
      format += "i"
      return unpack(format, buff.read())
      
    case "list":
      len = unpack('i', buff.read_length())
      return reader(buff, type_2, length=f'{len[0]}')
      
    case _:
      print('unsupported type')
      
    