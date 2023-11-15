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

// saving tensor metadata
void CTensor::save() {  
  buffer buf = buffer();
  int size = shape.size();

  buf.write(&size, 4);
  buf.write(&type, 2);
  buf.write(shape.data(), container_size(shape));

  file.write(buf.data(), container_size(buf), false);
}

void CTensor::load() {
  int size = 0;
  
  file.read(&size);
  file.read(&type);

  shape.resize(size);
  file.read(&shape);
}

#endif