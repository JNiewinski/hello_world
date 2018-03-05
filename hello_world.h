#ifndef HELLO_WORLD_H
#define HELLO_WORLD_H
#include <ostream>
using namespace std;

class hello_world
{
    public:
    hello_world();
    virtual ~hello_world();
    void print(ostream &buf);
};

#endif // HELLO_WORLD_H
