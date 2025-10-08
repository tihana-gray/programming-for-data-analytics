# program that reads a file and takes
# Author: Tihana Gray

FILENAME = "numbers.txt"
DATADIR = "../../data/"
FULLPATH = DATADIR + FILENAME

#print("Reading file:", FULLPATH)

with open(FULLPATH, 'rt') as fp:
    total = 0
    for line in fp:
        #print(f"{line.strip()}", end=' ')
        #print(f"has length {len(line)}")
        total += int(line)
    print(total)        
