#ifndef TENSOR
#define TENSOR

#include<map>

#include "tensor.h"
#include "bucket.cpp"
#include "buffer.cpp"

using namespace std;

CTensor::CTensor() {} 
CTensor::CTensor(string tensor_name) {
  root /= tensor_name;
  open(fullpath());
};

int CTensor::read(unsigned char* data, int num_of_tensors) {
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

void CTensor::put(buffer *data) {
  CBucket bucket = CBucket(root);
  bucket.write(data);
}

int CTensor::get(buffer *data, int rows_num) {
  CBucket b = CBucket(root);
  b.shape = shape;
  b.read(data, rows_num);
  return 0;
}

void CTensor::write(buffer data, int len) {
  CBucket bucket = CBucket();
  bucket.write(&data);
}

filesystem::path CTensor::fullpath() {
  return root / (root.filename() +=  extension);
}

#endif