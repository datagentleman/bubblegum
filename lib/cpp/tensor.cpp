#ifndef TENSOR
#define TENSOR

#include "tensor.h"
#include<map>

using namespace std;

CTensor::CTensor() {}

int CTensor::open(char* tensor_path) {
  file = File(tensor_path);
  return 0;
}

int CTensor::read(unsigned char* data, int num_of_tensors) {
  // calculate number of bytes to read
  auto elems_per_tensor = std::accumulate(shape.begin(), shape.end(), 1, std::multiplies<int>());
  auto num_of_bytes = num_of_tensors * elems_per_tensor * type;

  file.read(data);
  return 0;
}

void CTensor::save() {  
  buffer buf = buffer();
  
  // saving tensor metadata
  buf.write(shape.data(), container_size(shape));

  // buf.write(&type, 2);
  file.write(buf.data(), container_size(buf), true);
}

void CTensor::load() {
  type = int8;

  std::vector<int32_t> shape2;
  shape2.resize(5);
  file.read(shape2.data());
}

#endif