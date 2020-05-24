import re

mylines = "".join([line.rstrip() for line in open("3.txt")])

m = re.findall(r"(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])", mylines)

print(m)