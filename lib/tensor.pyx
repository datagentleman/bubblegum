# distutils: language = c++

# from lib.commands cimport ping

cdef extern from "cpp/tensor.cpp":
  cdef cppclass Stream:
    Stream()
    void from_fd(int fd) except +


cdef class Tensor:
  cpdef open(self, bytes tensor):
    return self.tensor.open(tensor)


  cpdef int write(self, bytes data):
    return self.tensor.write(data, len(data))


  cpdef read(self, int len):
    data = bytearray(len)
    self.tensor.read(data, len)
    return data


