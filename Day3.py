#!/usr/bin/python

import sys
from collections import namedtuple

#used to get a Pair structure with position labels
Pair = namedtuple("Pair", ["first", "last"])


def readFileIntoStr(fileName):
	with open(fileName) as f:
		content = f.readlines()
	
	#challenge only has 1 line, so returning 1st and only element
	#stripped to remove empty spaces or endlines
	return content[0].strip() 


#uses a set to count only unique houses; goes through the
#instruction list and follows each instruction one-by-one,
#changing Santa's coordinate based on the instruction
def PartOneSolution(instructions):
	coordinate = Pair(0,0)
	houses = {coordinate}
	
	for instruction in instructions:
		coordinate = followInstruction(coordinate,instruction)
		print "{} for {}".format(coordinate,instruction)
		houses.add(coordinate)
	
	print houses
	return len(houses)


def PartTwoSolution():
	pass

#changes the x or y pair based on the instruction
def followInstruction(coordinate, instruction):
	if instruction == '>':
		newCoord = Pair(coordinate.first+1,coordinate.last)
	elif instruction == '<':
		newCoord = Pair(coordinate.first-1,coordinate.last)
	elif instruction == '^':
		newCoord = Pair(coordinate.first,coordinate.last+1)
	else: #done as else to prevent non-declared newCoord error
	 	newCoord = Pair(coordinate.first,coordinate.last-1)
	return newCoord
      
      
#check for file argument
if len(sys.argv) != 2:
	raise Exception("Missing or too many command line arguments; needs a file argument!")

instructions = readFileIntoStr(sys.argv[1])
print PartOneSolution(instructions)