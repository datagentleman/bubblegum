# distutils: language = c++

from libcpp.vector cimport vector
from lib.commands  cimport *
from lib.tensor    cimport *
from cython        cimport cast


cdef extern from "cpp/buffer.cpp":
  cdef cppclass buffer:
    buffer()
    buffer(unsigned char*, int)

    int size()
    int read(unsigned char* data, int len)
    int write[T](T data, int len)
    unsigned char* data()

cdef extern from "cpp/utils.cpp":
    int container_size[T](T data)

cdef class Buffer:
  cdef buffer buf

  def __init__(self, bytes data):
    self.buf = buffer(data, len(data))

  def read(self, unsigned char* dst):
    pass


  def write(self, list data):
    t = Tensor()


  def data(self):
    cdef int len = self.buf.size()
    cdef unsigned char[:] data = <unsigned char[:len]> self.buf.data()

    return bytearray(data)