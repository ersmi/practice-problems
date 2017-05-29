Main: main.o Node.o BinarySearchTree.o Tree.o
	g++ -std=c++11 main.o -o Main

main.o: main.cpp
	g++ -std=c++11 -c main.cpp

Node.o: ../Node.cpp ../Node.h
	g++ -std=c++11 -c ../Node.cpp
	
Tree.o: ../Tree.cpp ../Tree.h
	g++ -std=c++11 -c ../Tree.cpp

BinarySearchTree.o: BinarySearchTree.cpp BinarySearchTree.h
	g++ -std=c++11 -c BinarySearchTree.cpp
	
clean:
	rm *.o
	rm Main.exe
