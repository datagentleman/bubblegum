# distutils: language = c++

cdef class Tensor:
  cpdef Tensor open(self, bytes path):
    self.tensor.open(path)
    return self

  cpdef int write(self, bytes data):
    # return self.tensor.write(data, len(data))
    pass

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