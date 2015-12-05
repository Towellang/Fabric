CC=gcc

fabric: towel.c towelfuncs.c
	$(CC) -o towel towel.c towelfuncs.c
