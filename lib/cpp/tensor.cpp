#include <atomic>
#include <iostream>
#include <string>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/socket.h>
#include <vector>
#include <numeric>

#include "utils.cpp"
#include "conn.cpp"
#include "buffer.cpp"

using namespace std;

// values are number of bytes per element
enum dtype { 
  int16 = 2,
};

class CTensor {
  public:
    // main file descriptor for our tensor
    int fd;

    dtype type = int16;

    // we need initial shape for tensor. We need it to calculate 
    // it's size and to assign id - required for update/remove operations.
    // We will also track how many rows we have for each bucket.
    //
    // Shape describes only rows - not the whole tensor.
    // Ex: when shape = 1 and we want let's say 100 rows, 
    // we will get output tensor {100 x 1}.
    // If shape = {2, 2} we will get {100 x 2 x 2}.
    //
    // For now it's hardcoded.
    std::vector<int> shape = {1};

    // this will allow us to use pwrite() in concurrent manner.
    // Each thread will get different offset for it's data and
    // we shouldn't have any conflicts ;)
    std::atomic<int> write_offset{0};

    CTensor() {}

    int open(char* tensor_path) {
      fd = ::open(tensor_path, O_CREAT| O_RDWR);

      int eof_offset = lseek(fd, 0, SEEK_END);
      write_offset.fetch_add(eof_offset, std::memory_order_relaxed);

      return fd;
    }

    int write(unsigned char* data, int len) {
      write_offset.fetch_add(len, std::memory_order_relaxed);
      return pwrite(fd, data, len, write_offset);
    }

    int read(unsigned char* data, int num_of_tensors) {
      // calculate number of bytes to read
      auto elems_per_tensor = std::accumulate(shape.begin(), shape.end(), 1, std::multiplies<int>());
      auto num_of_bytes = num_of_tensors * elems_per_tensor * type;

      return pread(fd, data, num_of_bytes, 0);
    }
};
