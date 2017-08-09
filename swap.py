import sys
import re

grid = []
width = 0
height = 1

(x,y) = (0,0)
(hor,ver) = (1,0)
skip = False
stringMode = False
charMode = False

active = 0
stacks = [[], []]

inBuffer = ''

if len(sys.argv)==1:
	raise Exception("No file specified.")
else:
	grid = [list(s) for s in open(sys.argv[1]).read().split('\n')]
	width = max(len(l) for l in grid)
	height = len(grid)
	for l in grid:
		while len(l)<width:
			l.append(' ')

def swap(char):
	ops = '''<v[/_s?"im+*(=,%@#$.~):-no'!x|\]^>'''
	if char in ops:
		return ops[~ops.find(char)]
	else:
		return char

def pop():
	if len(stacks[active]) > 0:
		return stacks[active].pop()
	else:
		return 0

def push(n):
	stacks[active].append(n)

def readchar():
	global inBuffer

	if inBuffer:
		c = inBuffer[0]
		inBuffer = inBuffer[1:]
		return c
	else:
		return sys.stdin.read(1) or 0
		

try:
	while True:
		cell = grid[y][x]
		skip = False
		if stringMode:
			if cell == '"':
				stringMode = False
			else:
				push(ord(cell))
		elif charMode:
			push(ord(cell))
			charMode = False
		else:
			if cell == '<': 
				hor = -1
			elif cell == '>': 
				hor = 1
			elif cell == 'v':
				ver = 1
			elif cell == '^':
				ver = -1
			elif cell == '/':
				(hor, ver) = (ver*-1, hor*-1)
			elif cell == '\\':
				(hor, ver) = (ver, hor)
			elif cell == '|':
				hor = hor*-1
			elif cell == '_':
				ver = ver*-1
			elif cell == '[':
				hor = abs(hor)*-1
			elif cell == ']':
				hor = abs(hor)
			elif cell == '?':
				if pop():
					skip = True
			elif cell == '!':
				if not pop():
					skip = True
			elif cell == 'x':
				break
			elif cell == '"':
				stringMode = True
			elif cell == "'":
				charMode = True
			elif cell == 'i':
				push(ord(readchar()))
			elif cell == 'o':
				sys.stdout.write(chr(pop()))
			#elif cell == 'm':
			#	input = ''
			#	c = readchar()
			#	while c in '0123456789' or (c == '-' and input == ''):
			#		input += c
			#		c = readchar()
			#	inBuffer += c
			#	push(int(input) if input else 0)
			#elif cell == 'n':
			#	sys.stdout.write(str(pop()))
			elif cell in '0123456789':
				push(int(cell))
			elif cell == '+':
				push(pop()+pop())
			elif cell == '-':
				push(pop()-pop())
			elif cell == '*':
				push(pop()*pop())
			elif cell == ':':
				push(pop()//pop())
			elif cell == '(':
				push(1 if pop()<pop() else 0)
			elif cell == ')':
				push(1 if pop()<pop() else 0)
			elif cell == '=':
				push(1 if pop()==pop() else 0)
			elif cell == '~':
				push(1 if pop()==pop() else 0)
			elif cell == ',':
				v = pop()
				push(v)
				push(v)
			elif cell == '.':
				pop()
			elif cell == '%':
				x = pop()
				y = pop()
				push(x)
				push(y)
			elif cell == '$':
				active = 1-active
			elif cell == '@':
				stacks[active] = stacks[active][-1:]+stacks[active][:-1]
			elif cell == '#':
				stacks[active] = stacks[active][1:]+stacks[active][:1]

		grid[y][x] = swap(cell)
		(x,y) = ((x+(hor+hor*skip))%width, (y+(ver+ver*skip))%height)

except:
	sys.stderr.write("Uh oh")
