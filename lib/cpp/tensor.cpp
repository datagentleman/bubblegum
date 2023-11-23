#ifndef TENSOR
#define TENSOR

#include<map>

#include "tensor.h"
#include "bucket.cpp"
#include "buffer.cpp"

using namespace std;

CTensor::CTensor() {}

int CTensor::open(char* tensor_path) {
  file = File(tensor_path);
  return 0;
}

int CTensor::read(unsigned char* data, int num_of_tensors) {
  // calculate number of bytes to read
  // auto elems_per_tensor = std::accumulate(shape.begin(), shape.end(), 1, std::multiplies<int>());
  // auto num_of_bytes = num_of_tensors * elems_per_tensor * type;
  file.read(data);
  return 0;
}

// saving tensor metadata
void CTensor::save() {  
  buffer buf = buffer();
  int size = shape.size();

  buf.write(&dtype);
  buf.write(&size);
  buf.write(&shape);

  file.write(buf.vec());
}

void CTensor::load() {
  int size = file.read_header();
  dtype.resize(size);
  file.read_data(&dtype, size);
  file.read(&shape);
}

void CTensor::write(buffer data, int len) {
  CBucket current_bucket = CBucket();
  current_bucket.write(&data);
}

#endif