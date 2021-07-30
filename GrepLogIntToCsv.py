import sys
import os
import re

strPatten = sys.argv[1]
strInFile = sys.argv[2]

strRegex = "(\d\d\d\d[-/]\d\d[-/]\d\d[T ]\d\d:\d\d:\d\d(\.\d+)?)\s.*{}".format(strPatten)

with open(strInFile) as fIn:
    for line in fIn:
        m = re.match(strRegex, line)
        if(m):
            strTime = m.group(1)
            nEnd = m.end(1)
            strOther = line[nEnd:]
            rgiVal = []
            rgToken = strOther.split(",")
            for token in rgToken:
                m2 = re.search("\d+", token)
                iVal = m2.group()
                rgiVal.append(iVal)

            print(strTime, end='')
            for iVal in rgiVal:
                print(",", end='')
                print(iVal, end='')
            print()
                
