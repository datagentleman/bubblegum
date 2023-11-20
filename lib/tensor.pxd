# distutils: language = c++

from libcpp.vector cimport vector
from libc.stdint   cimport int32_t
from libcpp.string cimport string

cdef extern from "cpp/tensor.cpp":
  cdef cppclass CTensor:
    vector[int32_t] shape
    string dtype

    CTensor() except +
    void save() except +
    void load() except +
    int open(char* path) except +
    int read(unsigned char *data, int len) except +
    int write(buffer data, int len) except +


cdef extern from "cpp/buffer.cpp":
  cdef cppclass buffer:
    buffer()

    int size()
    int read(unsigned char* data)
    int write(unsigned char* data, int len)
    unsigned char* data()


cdef class Tensor:
  cdef CTensor tensor
  
  cpdef Tensor open(self, bytes) 
  cpdef save(self)
  cpdef load(self)
  cpdef read(self, bytes, int) 
  cpdef write(self, bytes)
  