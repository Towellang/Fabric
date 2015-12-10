#!/usr/bin/env python2

import sys
import random
from string import join

STACK = []
LOOPS = [] # Loops are stacks too
PNT = 0
BREAK = False # Break mode

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
	"chr": lambda: sys.stdout.write( str( chr( STACK.pop() ) ) ),
	"=": lambda: logic(True) if STACK.pop() == STACK.pop() else logic(False),
	">": lambda: logic(True) if STACK.pop() > STACK.pop() else logic(False),
	"<": lambda: logic(True) if STACK.pop() < STACK.pop() else logic(False),
	"swap": lambda: swap(),
	"clone": lambda: STACK.extend(STACK),
	"grab": lambda: push(raw_input("")),
	"break": lambda: breakmode(),
#	"=": lambda: if STACK.pop() != STACK.pop(): PNT += 1,
	"end": lambda: leave()
}

def push(value): # ord & chr
	try: int(value)
	except:
		word = value[1:-1]
		for k,v in enumerate(word):
			STACK.append(ord(word[k]))
	else:
		STACK.append(int(value))

def loop():
	global STACK, LOOPS, PNT
	if STACK == [] or STACK[-1] == 0:
		LOOPS.pop()
	else:
		PNT = LOOPS[-1]

def breakmode():
	global BREAK
	BREAK = True

def swap():
	STACK[-1], STACK[-2] = STACK[-2], STACK[-1]

def logic(bvar):
	global PNT
	if bvar != True:
		PNT += 1

def prep(rawcode):
	for k,v in enumerate(rawcode):
		if v.startswith("#!") or v.startswith("//"):
			rawcode.pop(k)
	rawcode = " ".join(rawcode)
	return rawcode.split(" ")

def interpret(code):
	global STACK, LOOPS, PNT, BREAK
	while PNT < len(code):
		word = code[PNT]
		if BREAK:
			if word == "]":
				BREAK = False
		else:
			if word == "":
				PNT += 1
				continue
			if word.startswith("\"") and word.endswith("\""):
				push(word)
			elif word in ENV.keys():
				ENV[word]()
			elif word == "_SLEN":
				push(len(STACK))
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

def panic(msg):
	print("ERROR: " + msg + " on instruction #" + str(PNT + 1) + " (" + code[PNT] + ")")
	sys.exit(1)

def leave():
	print # Trailing newline to fix command prompt
	sys.exit(0)

if __name__ == "__main__":
	try:
		sys.argv[1]
	except:
		repl()	
	else:
		code = prep(open(sys.argv[1]).read().split("\n"))
		interpret(code)
	leave()
