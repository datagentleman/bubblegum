#include <atomic>
#include <iostream>
#include <string>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/socket.h>
#include <vector>

#include "utils.cpp"
#include "conn.cpp"
#include "buffer.cpp"

using namespace std;

class Ctensor {
  public:
    int fd;

    // this will allow us to use pweite() in concurrent manner.
    // Each thread will get different offset for it's data.
    std::atomic<int> write_offset{0};

    Ctensor() {}

    int open(char* tensor_path) {
      fd = ::open(tensor_path, O_RDWR);
      
      int eof_offset = lseek(fd, 0, SEEK_END);
      write_offset.fetch_add(eof_offset, std::memory_order_relaxed);

      cout << "write offset: "  << +write_offset << "\n";
      return fd;
    }

    int write(unsigned char* data, int len) {
      write_offset.fetch_add(len, std::memory_order_relaxed);
      return pwrite(fd, data, len, write_offset);
    }

    int read(unsigned char* data, int len) {
      return pread(fd, data, len, 0);
    }
};
