#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int mod100(int x) {
  // ensure result is always between 0–99
  int r = x % 100;
  if (r < 0)
    r += 100;
  return r;
}

void Part1(const std::string& file) {
  std::ifstream in(file);
  if (!in.is_open())
    return;

  std::vector<std::string> lines;
  std::string line;

  while (std::getline(in, line)) {
    lines.push_back(line);
  }

  int num = 50;
  int password = 0;

  for (const std::string& ln : lines) {
    std::string dist = ln.substr(1);
    int rot = std::stoi(dist);

    if (ln[0] == 'L')
      rot = -rot;

    num = mod100(num + rot);

    if (num == 0)
      password++;
  }

  std::cout << "Password for part 1: " << password << "\n";
}

void Part2(const std::string& file) {
  std::ifstream in(file);
  if (!in.is_open())
    return;

  std::vector<std::string> lines;
  std::string line;

  while (std::getline(in, line)) {
    lines.push_back(line);
  }

  int num = 50;
  int password = 0;

  for (const std::string& ln : lines) {
    std::string dist = ln.substr(1);
    int rot = std::stoi(dist);

    while (rot > 0) {
      if (ln[0] == 'R')
        num = mod100(num + 1);
      else
        num = mod100(num - 1);

      rot--;

      if (num == 0)
        password++;
    }
  }

  std::cout << "Password for part 2: " << password << "\n";
}

int main() {
  std::string file = "day01_cs/input.txt";
  Part1(file);
  Part2(file);
  return 0;
}
