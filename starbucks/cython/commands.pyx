# distutils: language = c++

from libcpp.string cimport string

cdef extern from "../cpp/conn.cpp":
  cdef cppclass conn:
    conn()
    conn(int)
    void write(void*, int)


cpdef void ping(int fd):
  cdef conn connection = conn(fd)
  cdef string pong = "PONG"

  connection.write(&pong, pong.length())

  