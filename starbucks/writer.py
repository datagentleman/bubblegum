from struct import pack

def write(data: any):
  match type(data).__name__:
    case 'int':
      return pack('i', data)
    
    case 'float':
      return pack('d', data)

    case 'str': 
      return write_len_data(data.encode())

    case 'list' | 'tuple':
      elems = b''.join([write(elem) for elem in data])
      
      data =  write(len(data))
      data += write(len(elems))
      data += elems

      return data
      
    case 'bytes': 
      return write_len_data(data)

    case _:        
      return write_len_data(data)  

def write_len_data(data: bytes) -> bytes:
  size = len(data).to_bytes(4, byteorder='little')
  return size + data
