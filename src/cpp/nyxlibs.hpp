#ifndef NYXLIBS_H
#define NYXLIBS_H

#include <iostream>
#include <vector>
#include <numeric>
#include <stdexcept>
#include <functional>

std::vector<int> range(int n);

template <typename... Args>
inline void print(Args &&...msg)
{
    ((std::cout << std::forward<Args>(msg) << (sizeof...(Args) > 1 ? " " : "")), ...);
    std::cout << std::endl;
}

std::string input(std::string prompt);

#endif