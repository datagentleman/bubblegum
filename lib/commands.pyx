# distutils: language = c++

from libcpp.string cimport string
from lib.tensor    cimport Tensor

cdef extern from "cpp/conn.cpp":
  cdef cppclass conn:
    conn()
    conn(int)
    void write(void*, int)


cpdef ping(int fd):
  Tensor().open(b'')
