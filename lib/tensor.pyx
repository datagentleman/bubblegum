# distutils: language = c++

cdef class Tensor:
  cpdef Tensor open(self, bytes tensor):
    self.tensor.open(tensor)
    return self


  cpdef int write(self, bytes data):
    return self.tensor.write(data, len(data))


  cpdef vector[int] shape(self):
    return self.tensor.shape


  cpdef read(self, int len):
    data = bytearray(len)
    self.tensor.read(data, len)
    return data


