# distutils: language = c++

from libcpp.string cimport string

cdef extern from "cpp/buffer.cpp":
  cdef cppclass buffer:
    buffer()
    int read(unsigned char* data)
    int write(void* data, int, bint header)
    unsigned char* data()

cdef extern from "cpp/bucket.cpp":
  cdef cppclass CBucket:
    CBucket() except*
    CBucket(string file_path) except*
    void write(buffer *src) except*
    void read(buffer *buff,  int len) except*


cdef class Bucket:
  cdef CBucket bucket
  cdef buffer  buf

  def __init__(self, string bucket_path):
    self.bucket = CBucket(bucket_path)
    self.buf = buffer()

  cpdef void write(self, bytes data):
    cdef unsigned char* ptr = data

    self.buf.write(ptr, len(data), False)
    self.bucket.write(&self.buf)

  cpdef bytes read(self, int len):
    buf = buffer()
    row_size = 4
    len = len * row_size;
    self.bucket.read(&buf, len)
    return bytes(buf.data()[:len])