# distutils: language = c++

cdef class Tensor:
  cpdef Tensor open(self, bytes path):
    self.tensor.open(path)
    return self


  cpdef write(self, bytes data):
    cdef buffer buf
    buf.write(data, len(data))
    self.tensor.write(buf, len(data))


  cpdef save(self):
    self.tensor.save()


  cpdef load(self):
    self.tensor.load()


  cpdef read(self, bytes dst, int len):
    data = bytearray(len)
    self.tensor.read(data, len)
    return data

 
  @property
  def shape(self):
    return self.tensor.shape


  @shape.setter
  def shape(self, val):
    self.tensor.shape = val
  
  
  @property
  def dtype(self):
    return self.tensor.dtype
    

  @dtype.setter
  def dtype(self, val):
    self.tensor.dtype = val