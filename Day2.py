import sys
import operator
import functools

#does list manipulation to extract the dimensional
#values from the input file
def getDimensionsFromFile(fileName):
	with open(fileName) as f:
		content = f.readlines()

	#strip to remove the empty spaces and endlines
	#split to get the actual numbers
	return [line.strip().split('x') for line in content] 



#returns the total amount of paper needed
def PartOneSolution(dimensionsList):
	rectAreasList = [getRectangleAreas(dimensions) for dimensions in dimensionsList]
	print rectAreasList
	#boxSurfaceAreas = [functools.reduce(operator.mul, rectAreas, 1) + min (rectAreas) for rectAreas in rectAreasList]
	#print boxSurfaceAreas


#returns a list containing the area of the rectangles
#along the width, height, and length
def getRectangleAreas(dimensions):
	
	#casts list from strings to ints
	print dimensions
	numList = [int(num) for num in dimensions]
	print numList
	#calculates each area necessary
	return [2*numList[0]*numList[1],2*numList[0]*numList[2],2*numList[1]*numList[2]]



#check for file argument
if len(sys.argv) != 2:
	raise Exception("Missing or too many command line arguments; needs a file argument!")

dimensionsList = getDimensionsFromFile( sys.argv[1] )

PartOneSolution(dimensionsList)
#print dimensionsList