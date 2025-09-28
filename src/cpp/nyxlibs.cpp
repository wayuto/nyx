#include "nyxlibs.hpp"

std::vector<int> range(int n)
{
    std::vector<int> arr(n);
    std::iota(arr.begin(), arr.end(), 0);
    return arr;
}

std::string input(std::string prompt = "")
{
    if (!prompt.empty())
        std::cout << prompt;
    std::string line;
    std::getline(std::cin, line);
    return line;
}