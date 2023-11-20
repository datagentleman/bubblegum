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

    CBucket() {}
    CBucket(std::string file_path) : File(file_path) { }

    void write(buffer *buff) {
      File::write(buff->vec());
    }
};

#endif