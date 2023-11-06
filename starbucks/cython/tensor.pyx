# distutils: language = c++

from libcpp.string cimport string
from libcpp.vector cimport vector
from libc.stdio    cimport printf
from libcpp        cimport bool

cdef extern from "../cpp/tensor.cpp":
  cdef cppclass Tensor:
    Tensor() 
    int  open(char* path) except +
    void print() except +

  
cdef extern from "../cpp/tensor.cpp":
  cdef cppclass Stream:
    Stream()
    void from_fd(int fd) except +
    

cdef class CTensor:
  cdef Tensor tensor

  def open(self, int fd, tensors: list(bytes)):
    cdef Stream stream
    stream.from_fd(fd)

    cdef char* ptr = tensors[0]
    self._open(ptr)
    return self.tensor.open(ptr)


  def print(self):
    self.tensor.print()


  cdef void _open(self, char* path):
    self.tensor = Tensor()
  
