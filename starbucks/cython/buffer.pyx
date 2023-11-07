# distutils: language = c++

cdef extern from "../cpp/buffer.cpp":
  cdef cppclass buffer:
    buffer()
    buffer(unsigned char*, int)

    int len()
    int read(unsigned char* data, int len)
    unsigned char* data()


cdef class Buffer:
  cdef buffer buf

  def __init__(self, bytes data):
    self.buf = buffer(data, len(data))

  def read(self, unsigned char* dst):
    pass

  def data(self):
    cdef len = self.buf.len()
    cdef unsigned char[:] view = <unsigned char[:len]> self.buf.data()
    return bytearray(view)