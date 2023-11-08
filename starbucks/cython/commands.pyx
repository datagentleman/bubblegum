# distutils: language = c++

from libcpp.string cimport string

cdef extern from "../cpp/conn.cpp":
  cdef cppclass conn:
    conn()
    conn(int)
    void write(string)

cpdef void ping(int fd):
  cdef conn connection = conn(fd)
  connection.write(string("PONG"))

  