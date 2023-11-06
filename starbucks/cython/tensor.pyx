# distutils: language = c++

from libc.stdio cimport printf
from libcpp     cimport bool

cdef extern from "../cpp/tensor.cpp":
  cdef cppclass Tensor:
    Tensor() 
    int open(char* path) except +
    int write(char *data, int
     len) except +

  
cdef extern from "../cpp/tensor.cpp":
  cdef cppclass Stream:
    Stream()
    void from_fd(int fd) except +
  

cdef class CTensor:
  cdef Tensor tensor

  def open(self, bytes tensor):
    return self.tensor.open(tensor)

  cpdef int write(self, bytes data):
    return self.tensor.write(data, len(data))
