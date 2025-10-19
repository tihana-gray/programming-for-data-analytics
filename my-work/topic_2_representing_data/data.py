# reading data.csv
# Author: Tihana Gray

import csv

FILENAME = "data.csv"
DATADIR = r"C:\Users\tihan\OneDrive\Desktop\ATU\programming-for-data-analytics\data\\"

#with open(DATADIR + FILENAME, "rt") as fp:
    #reader = csv.reader(fp, delimiter=",")
    #for line in reader:
        #print(line)

# data type is list

#with open(DATADIR + FILENAME, "rt") as fp:
    #reader = csv.reader(fp, delimiter=",")
    #linecount = 0

    #for line in reader:
        #if not linecount:  # first row ie header row
            #print(f"{line}\n-------------------")
        #else:  # all subsequent rows
            #print(line)
        #linecount += 1

#with open(DATADIR + FILENAME, "rt") as fp:
    #reader = csv.reader(fp, delimiter=",")
    #linecount = 0
    #total = 0
    #for line in reader:
        #if not linecount:  # first row (header)
            #pass
        #else:  # data rows
            #total += int(line[1])  # why 1? - converts string to int
        #linecount += 1
    #print(f"average is {total / (linecount - 1)}")  # why -1? - excludes header row

#with open(DATADIR + FILENAME, "rt") as fp:
    #reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    #linecount = 0
    #total = 0
    #for line in reader:
        #if not linecount:  # header
            #pass
        #else:
            #total += line[1]  # why 1? - same as above
        #linecount += 1
    #print(f"average is {total / (linecount - 1)}")  # why -1? - same as above)

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0

    for line in reader:
        total += line['age']
        # print(line)
        count += 1

    print(f"average is {total / count}")
      