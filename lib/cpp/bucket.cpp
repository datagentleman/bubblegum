#ifndef BUCKET
#define BUCKET

#include<map>
#include<mutex>

#include "file.cpp"

using namespace std;

// Main class for storing tensor data
class CBucket : public File {
  public:
    int id = 1;

    int header_start = 0;
    int data_start   = 400;

    std::atomic<int> *data_offset;
    std::atomic<int> *size;

    std::string extension = ".bucket";

    CBucket() {}
    CBucket(std::string path) {
      open(fullpath(path));

      data_offset = new std::atomic<int>(0);
      int eof_offset = lseek(fd, 0, SEEK_END);

      if(eof_offset < data_start) eof_offset = data_start;
      data_offset->fetch_add(eof_offset, std::memory_order_relaxed);

      load();
    }

    void save() {
      // std::lock_guard<std::mutex> lock(save_load);
      buffer buff = buffer();
      buff.write(size->load());
      File::write_at(buff.data(), container_size(buff), header_start);
    }

    void load() {
      int s = 0;
      File::read(&s);
      size = new std::atomic<int>(s);
    }

    // Write tensor rows to bucket
    void write(buffer *buff) {
      int len = container_size(buff->vec());
      int off = data_offset->fetch_add(len, std::memory_order_relaxed);

      File::write_at(buff->data(), len, off);
      save();
    }

    // Write tensor rows to bucket
    void write_at(buffer *buff, int offset) {
      File::write_at(buff->data(), container_size(buff->vec()), offset + data_start);
    }

    std::string fullpath(std::string path) {
      std::filesystem::path p{path};
      return p /= (std::to_string(id) + extension);
    }

    // Reading bytes from bucket file
    void read(buffer *buff, int number_of_rows, int bytesize, int offset=0) {
      buff->vec()->resize(number_of_rows);
      offset = data_start + offset;

      File::read_at(buff->data(), bytesize, offset);
    }
};

#endif