#include <chrono>

class Timer {
  public:
    Timer(const char* name) : name(name) {
      start = std::chrono::high_resolution_clock::now();
    }

    ~Timer() {
      auto end = std::chrono::high_resolution_clock::now();
      std::chrono::duration<double> seconds = std::chrono::duration_cast<std::chrono::duration<double>>(end - start);

      std::cout << name << " Execution Time: " << seconds.count() << " seconds" << std::endl;
    }

  private:
    const char* name;
    std::chrono::high_resolution_clock::time_point start;
};

#define TIMER_BEGIN(name) \
    { Timer timer##name(#name)
    
#define TIMER_END(name) \
    }
