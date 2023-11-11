# distutils: language = c++

from libcpp.vector cimport vector

cdef extern from "cpp/tensor.cpp":
  cdef cppclass CTensor:
    vector[int] shape

    CTensor() except +
    int open(char* path) except +
    int write(unsigned char *data, int len) except +
    int read(unsigned char *data, int len) except +


cdef class Tensor:
  cdef CTensor tensor

  cpdef Tensor open(self, bytes) 
  cpdef read(self, int) 
  cpdef int write(self, bytes)
  cpdef vector[int] shape(self)
