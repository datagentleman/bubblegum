#ifndef BUCKET
#define BUCKET

#include<map>

#include "file.cpp"

using namespace std;

// TODO: this will be map. Each bucket must have it's own counter. 
// static std::atomic<int> bucket_size(0);

// Main class for storing tensor data.
class CBucket : File {
  public:
    int id = 0;
    
    CBucket(std::string file_path="tensors/iris/1.bucket") { }
    
    void write(buffer *data) {

    }
};

#endif