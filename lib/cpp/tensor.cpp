#ifndef TENSOR
#define TENSOR

#include<map>

#include "tensor.h"
#include "bucket.cpp"
#include "buffer.cpp"

using namespace std;

CTensor::CTensor() {} 
CTensor::CTensor(char* tensor_path) : File(tensor_path) { }

int CTensor::read(unsigned char* data, int num_of_tensors) {
  // calculate number of bytes to read
  // auto elems_per_tensor = std::accumulate(shape.begin(), shape.end(), 1, std::multiplies<int>());
  // auto num_of_bytes = num_of_tensors * elems_per_tensor * type;
  File::read(data);
  return 0;
}

// saving tensor metadata
void CTensor::save() {  
  buffer buf = buffer();
  int size = shape.size();

  buf.write(&dtype);
  buf.write(&size);
  buf.write(&shape);

  File::write(buf.vec());
}

void CTensor::load() {
  int size = File::read_header();
  dtype.resize(size);

  // TODO: do something with this - there should be only one read()
  File::read_data(&dtype, size);
  File::read(&shape);
}

void CTensor::write(buffer data, int len) {
  CBucket bucket = CBucket();
  bucket.write(&data);
}

#endif