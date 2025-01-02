all: visualize visualize.o
visualize: visualize.o
	g++ -o visualize visualize.o -lsfml-graphics -lsfml-window -lsfml-system

visualize.o: visualize.cpp
	g++ -c visualize.cpp -lsfml-graphics -lsfml-window -lsfml-system

clean:
	rm -f visualize visualize.o
