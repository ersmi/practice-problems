Main: main.o Node.o BinaryTree.o
	g++ -std=c++11 main.o -o Main

main.o: main.cpp
	g++ -std=c++11 -c main.cpp

Node.o: ../Node.cpp ../Node.h
	g++ -std=c++11 -c ../Node.cpp
	
BinaryTree.o: BinaryTree.cpp BinaryTree.h
	g++ -std=c++11 -c BinaryTree.cpp

clean:
	rm *.o
	rm Main.exe