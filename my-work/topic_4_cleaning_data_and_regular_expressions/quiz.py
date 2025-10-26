# this is code for for the quiz
#Author: Tihana Gray

import re

regex = "^Hello [A-Z]"
filename = r"C:\Users\tihan\OneDrive\Desktop\ATU\programming-for-data-analytics\my-work\topic_4_cleaning_data_and_regular_expressions\sample-files\quiz.txt"

with open(filename) as quizFile:
    for line in quizFile:
        searchResult = re.search(regex, line)
        if (searchResult):
            matchingLine = line
            # I set the end to blank because each line will already have a \n
            print (matchingLine, end="")
