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

  property shape:
    def __get__(self):
      return self.tensor.shape

    def __set__(self, bytes val):
      self.shape = val
      self.tensor.shape = val
      