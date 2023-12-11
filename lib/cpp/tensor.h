#ifndef TENSOR_H
#define TENSOR_H

#include <atomic>
#include <map>
#include <iostream>
#include <string>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/socket.h>
#include <vector>
#include <numeric>

#include "buffer.cpp"
#include "utils.cpp"
#include "file.cpp"


std::map<std::string, int> DTYPES = {
  { "int8",  1 },
  { "int16", 2 }
};

using namespace std;

class CTensor: public File {
  public:
    string dtype = "int16";

    // we need initial shape for tensor. We need it to calculate 
    // it's size and to assign id - required for update/remove operations.
    // We will also track how many rows we have for each bucket.
    //
    // Shape describes only rows - not the whole tensor.
    // Ex: when shape = 1 and we want let's say 100 rows, 
    // we will get output tensor {100 x 1}.
    // If shape = {2, 2} we will get {100 x 2 x 2}.
    //
    // For now it's hardcoded.
    std::vector<int16_t> shape = {1};

    CTensor();
    CTensor(char* tensor_path);

    int read(unsigned char* data, int num_of_tensors);

    void save();
    void load();

    void write(buffer data, int len);
    int get(buffer *data, int num);
};

#endif
