#ifndef TENSOR
#define TENSOR

#include <atomic>
#include <iostream>
#include <string>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/socket.h>
#include <vector>
#include <numeric>

#include "tensor.h"
#include "buffer.cpp"
#include "utils.cpp"

using namespace std;

CTensor::CTensor() {}


int CTensor::open(char* tensor_path) {
  fd = ::open(tensor_path, O_CREAT| O_RDWR);

  int eof_offset = lseek(fd, 0, SEEK_END);
  write_offset.fetch_add(eof_offset, std::memory_order_relaxed);

  return fd;
}

int CTensor::write(unsigned char* data, int len, int offset=-1) {
  if(offset == -1) {
    write_offset.fetch_add(len, std::memory_order_relaxed);
    offset = write_offset;
  }

  return pwrite(fd, data, len, offset);
}

int CTensor::read(unsigned char* data, int num_of_tensors) {
  // calculate number of bytes to read
  auto elems_per_tensor = std::accumulate(shape.begin(), shape.end(), 1, std::multiplies<int>());
  auto num_of_bytes = num_of_tensors * elems_per_tensor * type;

  return pread(fd, data, num_of_bytes, 0);
}

void CTensor::save() {  
  buffer buf = buffer();

  // saving tensor metadata 
  buf.write(shape.data(), container_size(shape));
  buf.write(&type, type);

  write(buf.data(), container_size(buf));
}

#endif