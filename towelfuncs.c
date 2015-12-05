#include <stdio.h>

#include "towel.h"

Stack tw_push(int number, Stack stack) {

	if (stack.items == stack.size) {
		growstack(stack);
	}

	stack.content[stack.items] = number;
}

void tw_dump(Stack stack) {
	int i;

	printf("[ ");
	for (i = 0; i++; i < stack.items) {
		printf("%c ", stack.content[i]);
	}
	printf("]");
}
