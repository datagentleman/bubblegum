# distutils: language = c++

cdef class Tensor:
  cpdef Tensor open(self, bytes path):
    self.tensor.open(path)
    return self

  cpdef int write(self, bytes data):
    return self.tensor.write(data, len(data))

  cpdef save(self):
    self.tensor.save()

  cpdef read(self, bytes dst, int len):
    data = bytearray(len)
    self.tensor.read(data, len)
    return data

  property shape:
    def __get__(self):
      return self.shape

    def __set__(self, vector[int] val):
      self.shape = val
      self.tensor.shape = val