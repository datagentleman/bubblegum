#ifndef BUCKET
#define BUCKET

#include<map>

#include "file.cpp"

using namespace std;

static std::map<std::string, std::atomic<int> *> bucket_lengths;

// Main class for storing tensor data.
class CBucket : File {
  public:
    int id = 0;
    int data_start = 400;
    std::atomic<int> *data_offset;

    CBucket() {}
    CBucket(std::string file_path) : File(file_path) {
      data_offset = new std::atomic<int>(data_start);
    }

    void write(buffer *buff) {
      // write data
      int size = container_size(buff->vec());
      int off = file_offset->fetch_add(size, std::memory_order_relaxed);
      File::write_at(buff->vec(),  size, off);
    }
};

#endif