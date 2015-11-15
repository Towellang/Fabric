#include "towel.h"

Stack tw_push(int number, Stack stack) {

	if (stack.items == stack.size) {
		growstack(stack);
	}

	&stack.content[stack.items] = number;
}
