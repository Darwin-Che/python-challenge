import urllib.request
import cv2
import numpy as np

# fh = urllib.request.urlretrieve("http://www.pythonchallenge.com/pc/def/oxygen.png", "oxygen.png")
# im = cv2.imread("oxygen.png", 0)
import urllib.request
from io import BytesIO

zobj = BytesIO()
zobj.write(urllib.request.urlopen("http://pythonchallenge.com/pc/def/oxygen.png").read())
im = cv2.imread(zobj)

print(im.shape)
print(np.unique(im[47], return_counts=True))
print(([115,115]+list(im[47]))[::7])
print("".join([chr(e) for e in ([115,115]+list(im[47]))[::7]]))
print("".join([chr(e) for e in [105, 110, 116, 101, 103, 114, 105, 116, 121]]))

def myf(lst):
    ans = [lst[0]]
    prev = lst[0]
    for e in lst:
        if e == prev:
            continue
        else:
            ans.append(e)
            prev = e
    return ans

#print("".join([chr(e) for e in myf(im[47])]))
#print("".join([chr(e) for e in [105, 10, 16, 101, 103, 14, 105, 16, 121]]))
# arr = im[45,:]
# lst = []

# for i in range(len(arr)):
#     lst.append(chr(arr[i]))

# s = 0
# e = 0
# for i in range(len(lst)):
#     if lst[i] == '[' :
#         s = i
#         break
# for i in range(len(lst)):
#     if lst[i] == ']' :
#         e = i+1
#         break

# nlst = lst[s: e][::7]
# print(''.join(map(str,nlst)))
# # from the previous line
# ans = ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121])) 
# print(ans)