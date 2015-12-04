import sys
import operator
import functools

#does list manipulation to extract the dimensional
#values from the input file
def getDimensionsFromFile(fileName):
	with open(fileName) as f:
		content = f.readlines()

	#strip to remove the empty spaces and endlines
	#split to get the actual numbers and make them numbers
	return [map(int,line.strip().split('x')) for line in content] 



#returns the total amount of paper needed
def PartOneSolution(dimensionsList):
	rectAreasList = [getRectangleAreas(dimensions) for dimensions in dimensionsList]
	
	#takes each area list, sums the areas, multiplies the whole thing
	#by 2, and adds the smallest area to get needed SA 
	boxSurfaceAreas = [ 2*sum(rectAreas) + min (rectAreas) for rectAreas in rectAreasList]

	#returns the total area needed by adding the individual box requirements
	return sum(boxSurfaceAreas)


#returns a list containing the area of the rectangles
#along the width, height, and length
def getRectangleAreas(dimensions):
	
	#calculates each area necessary
	return [dimensions[0]*dimensions[1],dimensions[0]*dimensions[2],dimensions[1]*dimensions[2]]



#check for file argument
if len(sys.argv) != 2:
	raise Exception("Missing or too many command line arguments; needs a file argument!")

dimensionsList = getDimensionsFromFile( sys.argv[1] )

print PartOneSolution(dimensionsList)
#print dimensionsList