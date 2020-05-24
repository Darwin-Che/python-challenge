def myf(mdict, lst):
    for e in lst:
        if e in mdict:
            mdict[e] = mdict[e] + 1
        else:
            mdict[e] = 1
    return mdict

import urllib.request
fp = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
mytext = fp.readlines()
fp.close()

mylines = []

for lines in mytext:
    mylines = mylines + [(lines.decode("utf-8"))]

se = []

for linenumber, lines in enumerate(mylines):
    #print(linenumber,lines)
    if lines == "<!--\n":
        se.append(linenumber)
    if lines == "-->\n":
        se.append(linenumber)

mystr = ""

for lines in mylines[(se[2]+1):se[3]]:
    mystr = mystr + lines[:-1]

mydict = dict()

myf(mydict, list(mystr))

print(mydict)


