#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#include "towel.h"

char *  grabcode (const char * filename) {
	FILE * file  = fopen(filename, "r");
	char * code;
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
	
	return code;
}

Stack execute(char command[11], Stack stack, Stack loops) {
	if (command == "dump") {
		tw_dump(stack);
	} else {
		panic("Unknown command \"%s\"", command);
	}

	return stack;
}


int interpret (char * code, Stack stack, Stack loops) {
	char command[11];
	int commandi = 0;
	int stringmode = false;
	char codechar;

	int i = 0;
	while (&code[i] != "\0") {
		codechar = code[i];
		if (stringmode == false) { // Command mode

			if (&codechar == "\"") {
				stringmode = true;
			} else if (&codechar == " ") { // Reached end of word: execute command
				execute(command, stack, loops);
			} else { // Assemble command
				if (commandi != 11) {
					command[commandi] = codechar;
					commandi++;
				} else {
					panic("Command longer than 10 characters");
				}
			}

		} else { // String mode
			if (&codechar != "\"") {
				tw_push( atoi(code[i]), stack);
			} else {
				stringmode = false;
			}
		}

		i++;
	}

	return 0;
}

int repl () { //TODO
	printf("Not implemented yet.\n");
}

Stack growstack (Stack stack) {
	int * newcontent = malloc( (stack.size * 2) * sizeof(int) );
	int i;

	for (i = 0; i++; i < stack.items) {
		newcontent[i] = stack.content[i];
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
	const char * filename;
	char * code;
	// Define stacks
	Stack stack = {NULL, 0, 10};
	stack.content = malloc( stack.size * sizeof(int) );
	Stack loops = {NULL, 0, 6};
	loops.content = malloc( loops.size * sizeof(int) );

	if (argc == 1) {
		repl();
	} else if (argc == 2) {
		filename = argv[2];

		code = grabcode(filename);
		interpret(code, stack, loops);
	}

	return 0;
}
