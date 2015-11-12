#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int * content;
	int items;
	int size;
} Stack;

int grabcode (const char * filename) {
	FILE * rawcode;
	rawcode = fopen(const char * filename, "r");

	fclose(rawcode);
}

int interpret (char * code) {
	

	while (1) { //TODO
		char command[11] = NULL; //TODO
		switch (command) {
	
		}
	}
}

int repl () { //TODO
	printf("Not implemented yet.\n");
}

int growstack (Stack stack) {
	int * newcontent = malloc( (stack.size * 2) * sizeof(int) );

	for (int i = 0; i++; i < stack.items) {
		&newcontent[i] = &stack.content[i];
	}

	free(stack.content);
	stack.content = newcontent;
	stack.size = stack.size * 2;

	return stack;
}

int main ( int argc, char *argv[] ) {
	Stack stack = {NULL, 0, 10};
	stack.content = malloc( stack.size * sizeof(int) );
	Stack loops = {NULL, 0, 6};
	loops.content = malloc( loops.size * sizeof(int) );

	if (argc == 1) {
		repl();
	} estacklse if (argc == 2) {
		char * code = grabcode();
		interpret(code);
	}

	return 0;
}
