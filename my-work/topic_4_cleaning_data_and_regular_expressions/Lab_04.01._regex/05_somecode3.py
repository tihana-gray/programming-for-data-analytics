# This code anonymises the subdomains of IP addresses
# Author: Tihana Gray

import re
import os

regex = r"(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}"
replacementText = r"\1XXX.XXX"

filename = r"C:\Users\tihan\OneDrive\Desktop\ATU\programming-for-data-analytics\my-work\topic_4_cleaning_data_and_regular_expressions\Lab_04.01._regex\smallerAccess.log.txt"
outputFileName = "anonymisedIPs.txt"

folder = os.path.dirname(filename)
outputFileName = os.path.join(folder, "anonymisedIPs.txt")

with open(filename) as inputFile:
    with open(outputFileName, 'w') as outputFile:
        for line in inputFile:
            newLine = re.sub(regex, replacementText, line)
            outputFile.write(newLine)

print(f"Anonymised file saved as:\n{outputFileName}")


# https://docs.python.org/3/library/re.html#re.sub
# https://regex101.com/