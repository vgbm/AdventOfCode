#!/usr/bin/python

import sys
from hashlib import md5


#gets the match for 5 zeroes
def PartOneSolution(baseWord):
	return getFirstMatch(baseWord,5)


#gets the match for 6 zeroes
def PartTwoSolution(baseWord):
	return getFirstMatch(baseWord,6)


#returns the number which needs to be concatenated onto the
#baseWord in order to get the first numZeroes
#characters of the md5 hash to be zeroes
def getFirstMatch(baseWord, numZeroes):
	endNum = 0
	
	#search until the number is found
	while True:
		
		#hashes the concatenation of the word and number
		#then it pulls the first numZeroes characters
		#and compares it to a string of numZeroes characters
		#which only contains zeroes; returns endNum if a match was found
		if md5(baseWord+str(endNum)).hexdigest()[:numZeroes] == ('0'*numZeroes):
			return endNum

		endNum+=1


#checking if a base word was provided
if len(sys.argv) != 2:
	raise Exception("Missing or too many command line arguments; need the base word!")

baseWord = sys.argv[1]
print "The first match for five zeroes is {}".format(PartOneSolution(baseWord))
print "The first match for six zeroes is {}".format(PartTwoSolution(baseWord))