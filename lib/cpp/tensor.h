#ifndef TENSOR_H
#define TENSOR_H

using namespace std;

// values are number of bytes per element
enum dtype { 
  int16 = 2,
};

class CTensor {
  public:
    // main file descriptor for our tensor
    int fd;

    dtype type = int16;

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
    std::vector<int> shape = {1};

    // this will allow us to use pwrite() in concurrent manner.
    // Each thread will get different offset for it's data and
    // we shouldn't have any conflicts ;)
    std::atomic<int> write_offset = 0;

    CTensor();
    
    int open(char* tensor_path);
    int write(unsigned char* data, int len, int offset);
    int read(unsigned char* data, int num_of_tensors);

    void save();
};

#endif
