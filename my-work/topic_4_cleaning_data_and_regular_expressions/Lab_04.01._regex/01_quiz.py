# this is code for the quiz

import re

regex = ".*"
filename = "./sample-files/quiz.txt"

with open(filename) as quizFile:
	for line in quizFile:
		searchResult = re.search(regex, line)
		if (searchResult):
			matchingLine = line
			
			print(matchingLine, end="")
			
