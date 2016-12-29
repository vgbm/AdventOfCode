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


#single santa visiting houses based on the instruction list
def PartOneSolution(instructions):
	housesSet = getHousesVisited(instructions)
	return len(housesSet)


def PartTwoSolution(instructions):
	
	#santa begins at first instruction an goes every other
	santaHouses = getHousesVisited(instructions[::2])
	
	#roboSanta begins at the second instruction and goes every other
	roboHouses = getHousesVisited(instructions[1::2])
	
	#unions the sets to weed out repeats and then pulls the length to get overall num of houses
	return len( set().union(santaHouses,roboHouses) )


#uses a set to count only unique houses; goes through the
#instruction list and follows each instruction one-by-one,
#changing Santa's coordinate based on the instruction
def getHousesVisited(instructions):
	coordinate = Pair(0,0)
	houses = {coordinate}
	
	for instruction in instructions:
		coordinate = followInstruction(coordinate,instruction)
		houses.add(coordinate)
	
	return houses
      
      
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
print "Santa alone visits {} houses".format(PartOneSolution(instructions))
print "Santa and RoboSanta visit {} houses".format(PartTwoSolution(instructions))