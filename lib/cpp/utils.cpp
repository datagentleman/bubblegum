#ifndef UTILS
#define UTILS 

#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

// display unsigned char*
template <typename T>
void display(T data, int size, bool as_bytes=false) {
  if(as_bytes) {
    for(int i=0; i < size; i++) {
      std::cout << std::hex << "\\x" << static_cast<int>(data[i]);
    }
    return;
  } 

  for(int i=0; i < size; i++) {
    std::cout << data[i];
  }
}

// this should work for every object that implements [] and size()
template <typename T>
int container_size(T data) {
  return sizeof(data[0]) * data.size();
}

template <typename T>
int container_size(T *data) {
  return sizeof(data->front()) * data->size();
}

#endif