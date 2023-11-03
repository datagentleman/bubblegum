# distutils: language = c++

from libcpp.string cimport string

cdef extern from "../cpp/tensor.cpp":
  cdef cppclass Tensor:
    void open()


cdef class CTensor:
  cpdef string hello(self):
    cdef string hello = "hello world"
    return hello
