import urllib.request
from PIL import ImageDraw, Image
# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.
username = "huge"
password = "file"
top_level_url = "http://www.pythonchallenge.com/pc/return/good.html"
password_mgr.add_password(None, top_level_url, username, password)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
opener.open(top_level_url)

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)

fp = urllib.request.urlopen(top_level_url)
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

mylines = mylines[se[2]+1:se[3]]

# for n,lines in enumerate(mylines):
#    print(n, end="   ")
#    print(lines)

first = mylines[3:21]
second = mylines[23:28]

def stlst(t):
    ans=[]
    for x in t:
        ans= ans + (x.split(",")[:-1])
    return ans

first = stlst(first)
second = stlst(second)
result = first + second 

mytup = [(int(result[i]), int(result[i+1])) for i in range(0, len(result)) if i%2 == 0]

im = Image.new('RGB', (500, 500), (128, 128, 128))
draw = ImageDraw.Draw(im)
draw.polygon(mytup)
im.show()



