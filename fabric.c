#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct {
	int * content;
	int items;
	int size;
} Stack;

char *  grabcode (const char * filename) {
	FILE * file  = fopen(filename, "r");
	char * code;
	char * codearray;
	size_t n = 0;
	int c;

	if (file == NULL) return NULL;

	fseek(file, 0, SEEK_END);
	long f_size = ftell(file);
	fseek(file, 0, SEEK_SET);
	code = malloc(f_size);

	while ((c = fgetc(file)) != EOF) {
		code[n++] = (char)c;
	}

	code[n] = "\0";

	fclose(file);
	
	int i = 0;
	while (&code[i] != "\0") {
		
	}

	return codearray;
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

int panic(char * msg) {
	printf("An error occured: %s", &msg);
}

int main ( int argc, char *argv[] ) {
	// Define stacks
	Stack stack = {NULL, 0, 10};
	stack.content = malloc( stack.size * sizeof(int) );
	Stack loops = {NULL, 0, 6};
	loops.content = malloc( loops.size * sizeof(int) );

	if (argc == 1) {
		repl();
	} estacklse if (argc == 2) {
		const char * filename = argv[2];

		char * code = grabcode(filename);
		interpret(code);
	}

	return 0;
}
