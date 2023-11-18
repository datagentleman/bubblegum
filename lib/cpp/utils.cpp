#ifndef UTILS
#define UTILS 

#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

// reading 2 bytes and converting them to uint16
uint16_t to_uint16(char* bytes, bool big_endian=true) {
  if (big_endian) {
    return (bytes[0] << 8) | bytes[1];
  }

  return 0;
}

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

#endif