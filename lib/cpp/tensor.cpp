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
  load();
};

int CTensor::read(unsigned char* data, int num_of_tensors) {
  File::read(data);
  return 0;
}

// saving tensor metadata
void CTensor::save() {
  buffer buf = buffer();
  int size = shape.size();

  buf.write(&name);
  buf.write(&dtype);
  buf.write(&size);
  buf.write(&shape);
  
  File::write(buf.vec());
}

void CTensor::load() {
  buffer buf = buffer();
  File::read(buf.vec());

  buf.read(&name);
  buf.read(&dtype);
  buf.read(&shape);
}

void CTensor::put(buffer *data) {
  CBucket bucket = CBucket(root);
  bucket.write(data);
}

void CTensor::set(buffer *data, int index) {
  CBucket bucket = CBucket(root);
  
  index = index_offset(index);
  bucket.write_at(data, index_offset(index));
}

// Get rows from tensor
int CTensor::get(buffer *dst, int number_of_rows) {
  CBucket b = CBucket(root);

  int total_bytesize = number_of_rows * row_size();
  int total_items    = number_of_rows * items_per_row();

  b.read(dst, total_items, total_bytesize);
  return 0;
}

// Calculate number of items per row
int CTensor::items_per_row() {
  return std::accumulate(shape.begin(), shape.end(), 1, std::multiplies<int>());
}

// Calculate number of bytes per row
int CTensor::row_size() {
  int item_size = DTYPES[dtype];
  return items_per_row() * item_size;
}

// Get index offset
int CTensor::index_offset(int index) {
  index = std::max(index - 1, 0);
  return index * row_size();
}

void CTensor::write(buffer data, int len) {
  CBucket bucket = CBucket();
  bucket.write(&data);
}

filesystem::path CTensor::fullpath() {
  return root / (root.filename() +=  extension);
}

#endif