# This is matching IP addresses in my smallerAccess.log.txt file
# Author: Tihana Gray

import re
regex = "\d+\.\d+\.\d+\.\d+"

filename = "C:\\Users\\tihan\\OneDrive\\Desktop\\ATU\\programming-for-data-analytics\\my-work\\topic_4_cleaning_data_and_regular_expressions\\Lab_04.01._regex\\smallerAccess.log.txt"

with open(filename) as inputFile:
    for line in inputFile:
        foundTextList = re.findall(regex, line)
        if (len(foundTextList)!= 0):
            #print(foundTextList)
            foundText = foundTextList[0]
            print(foundText)
            # if I did not want the [] at the beginning and end
            print(foundText[1:-1])