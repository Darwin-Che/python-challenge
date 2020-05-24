import urllib.request
import re
addr = "63579" 
for i in range(400):
    fp = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+addr)
    mytext = "".join([line.decode("utf-8") for line in fp.readlines()])
    lookfor = re.findall(r"the next nothing is ([0-9]*)", mytext)
    if len(lookfor) != 1: break
    print(i, mytext)
    addr = lookfor[0]
    fp.close()