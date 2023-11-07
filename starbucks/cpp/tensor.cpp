#include <iostream>
#include <string>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/socket.h>
#include <atomic>
#include <vector>

#include "utils.cpp"
#include "conn.cpp"

using namespace std;

class Tensor {
  public:
    int fd;

    Tensor(){}

    int open(char* tensor_path) {
      fd = ::open(tensor_path, O_RDWR);
      return fd;
    }

    int write(unsigned char* data, int len) {
      return pwrite(fd, data, len, 0);
    }

     void read(unsigned char* data, int len) {
      pread(fd, data, len, 0);
    }
};
