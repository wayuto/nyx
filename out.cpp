#include "/home/wan/nyx/src/cpp/nyxlibs.hpp"
auto f(auto x)
{
    if ((x <= 1))
    {
        return x;
    }
    else
    {
        return (f((x - 1)) + f((x - 2)));
    }
}
int main(void)
{
    auto x = f(10);
    print(x);
}