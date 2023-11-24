# distutils: language = c++

from libcpp.vector cimport vector
from lib.commands  cimport *
from lib.tensor    cimport *
from cython        cimport cast


cdef extern from "cpp/buffer.cpp":
  cdef cppclass buffer:
    buffer()

    int size()
    int read(unsigned char* data)
    int write(void* data, int len)
    unsigned char* data()

cdef extern from "cpp/utils.cpp":
    int container_size[T](T data)
    int display[T](T data, int size, bool)


cdef class Buffer:
  cdef buffer buf

  def __init__(self):
    self.buf = buffer()


  def read(self, bytearray dst):
    self.buf.read(dst)


  def write(self, bytes data):
    cdef unsigned char* ptr = data
    self.buf.write(ptr, len(data))
    
  def data(self):
    cdef int len = self.buf.size()
    cdef unsigned char[:] data = <unsigned char[:len]> self.buf.data()

    return bytearray(data)