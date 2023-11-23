#ifndef BUCKET
#define BUCKET

#include<map>
#include<mutex>

#include "file.cpp"

using namespace std;

static std::map<std::string, std::atomic<int> *> bucket_lengths;

// Main class for storing tensor data.
class CBucket : File {
  public:
    int id = 0;
    
    int header_start = 0;
    int data_start   = 400;

    std::atomic<int> *data_offset;
    // std::mutex save_load;

    CBucket() {}
    CBucket(std::string file_path) : File(file_path) {
      data_offset = new std::atomic<int>(0);
      data_offset->fetch_add(data_start, std::memory_order_relaxed);
    }

    // void save() {
      // std::lock_guard<std::mutex> lock(save_load);
      // buff = buffer()
      // buff.write(size);
      // File::write_at(buff->data(), container_size(buf.vec()), header_start);
    // }

    void write(buffer *buff) {
      int size = container_size(buff->vec());
      int off = data_offset->fetch_add(size, std::memory_order_relaxed);
      
      File::write_at(buff->data(), size, off);
      
      // calculate ids for given offset
      // TODO: move to method
      // off -= data_start;
      // off += size;

      // int row_size = 4;
      // int num_of_ids = size / row_size;

      // int first_id = off / row_size;
      // int last_id  = first_id + num_of_ids;

      // std::vector<int> ids(num_of_ids);
      // for(int i=first_id; i <= last_id; i++) {
      //   ids.push_back(i);
      // }
    }

    // read number of tensor rows
    void read(buffer *buff, int len) {
      buff->vec()->resize(len);

      int offset = data_start + len;
      File::read_at(buff->data(), len, data_start);
    }
};

#endif