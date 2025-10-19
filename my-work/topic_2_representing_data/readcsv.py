#program that reads a file and takes
#Author: Tihana Gray

import csv

FILENAME = "students.csv"
DATADIR = "../../data/"
FULLPATH = DATADIR + FILENAME

#print("Reading file:", FULLPATH)

with open(FULLPATH, 'rt') as fp:
    #for line in fp:
    #    print(line, end="")
    reader = csv.reader(fp, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    linenumber = 0
    for line in reader:
        if linenumber:
            #print(line)
            total += int(line[1]) # the ages have quotes so are read in as strings
            
        linenumber += 1
    print(total)
