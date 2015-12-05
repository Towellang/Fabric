// Structs
typedef struct {
	int * content;
	int items;
	int size;
} Stack;


// Towel commands
Stack tw_push(int number, Stack stack);
void tw_dump(Stack stack);
