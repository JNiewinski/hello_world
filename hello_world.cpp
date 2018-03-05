#include "hello_world.h"
#include <iostream>
using namespace std;

hello_world::hello_world()
{
}

hello_world::~hello_world()
{
}

void hello_world::print(ostream &buf)
{
    buf<<"Hello world";
}
