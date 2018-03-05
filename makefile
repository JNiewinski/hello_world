all: hello_world.out
	rm *.o
hello_world.out: main.o hello_world.o
	g++ main.o hello_world.o -o hello_world.out
main.o: main.cpp hello_world.h
	g++ -c main.cpp
hello_world.o: hello_world.cpp hello_world.h
	g++ -c hello_world.cpp
clean:
	rm -rf *.o *.out
