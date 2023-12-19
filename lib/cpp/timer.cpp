#include <chrono>

using namespace std::chrono;

class Timer {
  public:
    Timer(const char* name) : name(name) {
      start = high_resolution_clock::now();
    }

    ~Timer() {
      auto end = high_resolution_clock::now();
      auto seconds = duration_cast<duration<double>>(end - start);

      std::cout << name << " Execution Time: " << seconds.count() << " seconds" << std::endl;
    }

  private:
    const char* name;
    high_resolution_clock::time_point start;
};

#define TIMER_BEGIN(name) \
    { Timer timer##name(#name)

#define TIMER_END(name) \
    }
