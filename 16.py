from PIL import Image
import numpy
from collections import Counter
from urlimg import *

def repeatedsublist(lst):
    max = 0
    ans = lst[0]
    cur = 0
    pre = lst[0]
    for i in range(len(lst)):
        if lst[i] == pre:
            cur += 1
        else:
            if cur >= max:
                max = cur
                ans = pre
            pre = lst[i]
            cur = 1
    if cur >= max:
        max = cur
        ans = pre
    return ans

url = 'http://www.pythonchallenge.com/pc/return/mozart.html'
x = urlimg(url, 'huge', 'file')
x.allimg()
x.dimg(0)

im = Image.open('mozart.gif')

print(Counter([repeatedsublist(lines) for lines in numpy.asarray(im)]).most_common())
# output [(195, 450), (225, 17), (9, 12), (60, 1)]

# test if 195 is
n = Image.new('P', (10, 10), 195)
n.putpalette(im.getpalette())
n.save("16-1.gif")

# rotate by putting the first occurence of pink to the first col
# print([numpy.where(x == 195)[0][0] for x in numpy.array(im)])
arr = numpy.array([numpy.roll(x, -numpy.where(x == 195)[0][0]) for x in numpy.array(im)])
ans = Image.fromarray(arr, mode = 'P')
ans.putpalette(im.getpalette())
ans.save("16-2.gif")




