# distutils: language = c++

from libcpp.string cimport string

cdef extern from "cpp/commands.cpp":
  void tput(int fd)
  void tget(int fd)
  void tset(int fd)

cpdef t_put(int fd):
  tput(fd)

cpdef t_get(int fd):
  tget(fd)

cpdef t_set(int fd):
  tset(fd)
