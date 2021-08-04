import sys
import os
import re

strInFile = sys.argv[1]

rgIndexes = []
for i in range(2,len(sys.argv)):
    arg = sys.argv[i]
    val = int(arg)
    rgIndexes.append(val)
rgIndexes.sort()

with open(strInFile) as fIn:
    for line in fIn:
        line = line.rstrip("\n")
        rgToken = line.split(",")
        for index in reversed(rgIndexes):
            rgToken.pop(index)
        line1 = ",".join(rgToken)
        print(line1)