# distutils: language = c++

from libcpp.string cimport string
from lib.tensor    cimport Tensor

cdef extern from "cpp/conn.cpp":
  cdef cppclass conn:
    conn()
    conn(int)
    void write(void*, int)

cdef extern from "cpp/commands.cpp":
    void tensor_put(int fd)


cpdef ping(int fd):
  Tensor().open(b'')

cpdef put(int fd):
  tensor_put(fd)