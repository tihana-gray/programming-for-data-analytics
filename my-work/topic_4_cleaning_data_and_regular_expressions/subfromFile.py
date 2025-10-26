# This is code anonymise the sub domains of ip addresses 
# Author: Tihana Gray

import re

#regex = r"\d{1,3}\.\d{1,3} " # this will find other numbers apart from ips
regex =  r"(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}"  # we make a group at the beginning to keep
replacementText="\\1XXX.XXX " # note the space at the end to match above
filename = r"C:\Users\tihan\OneDrive\Desktop\ATU\programming-for-data-analytics\my-work\topic_4_cleaning_data_and_regular_expressions\sample-files\quiz.txt"
outputFileName = "anonymisedIPs.txt"

with open(filename) as inputFile:
    with open(outputFileName, 'w') as outputFile:
        for line in inputFile:
            # for debugging
            #foundText = re.search(regex, line).group()
            #print(foundText)
            newLine = re.sub(regex, replacementText, line)
            outputFile.write(newLine)
            