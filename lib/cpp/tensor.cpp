#ifndef TENSOR
#define TENSOR

#include "tensor.h"

using namespace std;

CTensor::CTensor() {}

int CTensor::open(char* tensor_path) {
  file = File(tensor_path);
  return 0;
}

int CTensor::write(unsigned char* data, int len, int offset=-1) {
  return file.write(data, len);
}

int CTensor::read(unsigned char* data, int num_of_tensors) {
  // calculate number of bytes to read
  auto elems_per_tensor = std::accumulate(shape.begin(), shape.end(), 1, std::multiplies<int>());
  auto num_of_bytes = num_of_tensors * elems_per_tensor * type;


  return file.read(data, num_of_bytes, 0);
}

void CTensor::save() {  
  buffer buf = buffer();

  // saving tensor metadata
  buf.write(shape.data(), container_size(shape));
  buf.write(&type, type);

  write(buf.data(), container_size(buf));
}

void CTensor::load() {  
  buffer buf = buffer();
}

#endif