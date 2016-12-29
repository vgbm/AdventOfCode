#!/usr/bin/python

import sys

def readFileIntoStr(fileName):
	with open(fileName) as f:
		content = f.readlines()

	return content[0] #challenge only has 1 line, so returning 1st and only element


#calculates the difference in ( versus )
def PartOneSolution(directions):
	#inefficient but simple
	return directions.count('(') - directions.count(')')


#finds the first index putting Santa in the basement (Accumulator goes negative)
def PartTwoSolution(directions):
	
	accum = 0 #will be incremented or decremented according to paren
	index = 1 #index of accum (character position)
	for ch in directions:
		if ch == '(':
			accum+=1
		elif ch == ')':
			accum-=1
		if accum<0:
			return index
		index+=1

	return -1

#check for file argument
if len(sys.argv) != 2:
	raise Exception("Missing or too many command line arguments; needs a file argument!")

directions = readFileIntoStr(sys.argv[1])

print "Santa needs to go to floor " + str(PartOneSolution(directions))

if PartTwoSolution(directions) != -1:
	print "Santa enters the basement on instruction " + str(PartTwoSolution(directions))
