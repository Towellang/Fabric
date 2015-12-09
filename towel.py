#!/usr/bin/env python2

import sys
import random
from string import join

STACK = []
LOOPS = [] # Loops are stacks too
PNT = 0

ENV = {
	"[": lambda: LOOPS.append(PNT),
	"]": lambda: loop(),
	"drop": lambda: STACK.pop(),
	"dup": lambda: push(str(STACK[-1])) if STACK != [] else panic("Tried dupping on an empty stack"),
	"rand": lambda: push(str(random.randint(0, 99))), # Converted to string so push doesn't lose its shit
	"dump": lambda: sys.stdout.write(str(STACK)),
	"rev": lambda: STACK.reverse(),
	"raise": lambda: STACK.insert(0, STACK.pop()),
	"lower": lambda: STACK.insert(len(STACK), STACK.pop(0)),
	"add": lambda: push(STACK.pop() + STACK.pop()),
	"+": lambda: push(STACK.pop() + STACK.pop()),
	"sub": lambda: push(-1 * STACK.pop() + STACK.pop()),
	"-": lambda: push(-1 * STACK.pop() + STACK.pop()),
	"put": lambda: sys.stdout.write( str( STACK.pop() ) ),
	"chr": lambda: sys.stdout.write( str( chr( STACK.pop) ) ),
	"end": lambda: sys.exit(0)
}

def push(value): # ord & chr
	try: int(value)
	except:
		word = value[1:-1]
		for i in word:
			STACK.append(ord(word[i]))
	else:
		STACK.append(int(value))

def loop():
	global STACK, LOOPS, PNT
	if STACK == [] or STACK[-1] == 0:
		LOOPS.pop()
	else:
		PNT = LOOPS[-1]

def panic(msg):
	print("ERROR: " + msg + " on instruction #" + str(PNT + 1) + " (" + code[PNT] + ")")

def prep(rawcode):
	rawcode = " ".join(rawcode)
	return rawcode.split(" ")

def interpret(code):
	global STACK, LOOPS, PNT
	while PNT < len(code):
		word = code[PNT]
		if word == "":
			PNT += 1
			continue
		if word.startswith("\"") and word.endswith("\""):
			push(word)
		elif word in ENV.keys():
			ENV[word]()
		else:
			try: int(word)
			except: panic("Unknown command or broken value")
			else: push(word)

		PNT += 1

def repl():
	print("Welcome to the REPL")
	code = []
	while True:
		code.append(prep(raw_input(">>> ").split(" ")))
		interpret(code)
	print("Go away! No REPL here!")

if __name__ == "__main__":
	try:
		sys.argv[1]
	except:
		repl()	
	else:
		code = prep(open(sys.argv[1]).read().split("\n"))
		interpret(code)
	
	print # Trailing newline to fix command prompt
