# distutils: language = c++

cdef extern from "../cpp/tensor.cpp":
  cdef cppclass Tensor:
    Tensor() 
    int open(char* path) except +
    int write(unsigned char *data, int len) except +
    void read(unsigned char *data, int len) except +

  
cdef extern from "../cpp/tensor.cpp":
  cdef cppclass Stream:
    Stream()
    void from_fd(int fd) except +
  

cdef class CTensor:
  cdef Tensor tensor

  def open(self, bytes tensor):
    return self.tensor.open(tensor)


  cpdef int write(self, bytes data):
    return self.tensor.write(data, len(data))
    

  cpdef read(self, int len):
    data = bytearray(len)
    self.tensor.read(data, len)
    return data


