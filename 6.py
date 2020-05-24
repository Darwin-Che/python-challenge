import re,zipfile
filename = '90052.txt'
f1 = open('channel/'+filename)
channel = zipfile.ZipFile('channel.zip', 'r')
ans = ""
while 1:
    text = "".join(f1.readlines())
    print(text)
    num = re.findall(r"Next nothing is ([0-9]*)", text)
    if len(num) == 0:
        print("there is no nothing")
        break
    ans = ans + channel.getinfo(num[0]+'.txt').comment.decode()
    filename = num[0]+'.txt'
    f1.close()
    f1 = open('channel/'+filename)
print(ans)

# curl -s http://www.pythonchallenge.com/pc/def/channel.zip>tmp.zip
# number=$(unzip -ap tmp readme.txt|egrep -o [0-9]+$)
# while [ -n "$number" ]; do
#         echo -n "$(unzip -l tmp|egrep -A 1 $number.txt|sed -nE '2 s/(.).*/\1/p')";
#         number=$(unzip -ap tmp $number.txt|egrep -o [0-9]+$);
# done;
# rm tmp.zip;