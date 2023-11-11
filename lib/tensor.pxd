# distutils: language = c++

cdef extern from "cpp/tensor.cpp":
  cdef cppclass Ctensor:
    Ctensor() except +
    int open(char* path) except +
    int write(unsigned char *data, int len) except +
    int read(unsigned char *data, int len) except +


cdef class Tensor:
  cdef Ctensor tensor

  cpdef open(self, bytes) 
  cpdef read(self, int) 
  cpdef int write(self, bytes)
