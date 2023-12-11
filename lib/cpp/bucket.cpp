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
    
    // TODO: hardcoded, only temporary
    int row_size = 4;
    std::vector<int16_t> shape = {1};

    std::atomic<int> *data_offset;
    std::atomic<int> *size;

    CBucket() {}

    CBucket(std::string file_path) : File(file_path) {
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

    // Write tensor data to bucket
    void write(buffer *buff) {
      int len = container_size(buff->vec());
      int off = data_offset->fetch_add(len, std::memory_order_relaxed);

      File::write_at(buff->data(), len, off);

      size->fetch_add((len/row_size));
      save();
    }

    // Read number of rows
    // TODO: later we can use sendfile instead 
    void read(buffer *buff, int rows_num) {
      buff->vec()->resize(rows_num);

      // TODO: 4 is hardcoded for now - it will be replaced with dtype size
      int bytes_to_read = rows_num * num_of_elems() * 4;
      std::cout << "BYTES TO READ: " << +bytes_to_read << "\n"; 
      File::read_at(buff->data(), bytes_to_read, data_start);
    }

  private:
    int num_of_elems() {
      auto begin = std::begin(shape);
      auto end   = std::end(shape);
      
      return std::accumulate(begin, end, 1, std::multiplies<int16_t>());
    }
};

#endif