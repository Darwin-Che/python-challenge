# a = [1, 11, 21, 1211, 111221, 
# https://en.wikipedia.org/wiki/Look-and-say_sequence

import math

# las :: int -> int
def las(pre):
    ans = []
    prev = ""
    for i in str(pre):
        if (prev == ""):
            ans = [i]
            prev = i
        elif (i == prev):
            ans = ans[:-1] + [(ans[-1]+i)]
            prev = i
        else :
            ans = ans + [i]
            prev = i
    nexts = "".join(str(len(s))+s[0] for s in ans)
    return int(nexts)

def gen(start, n):
    if (n == 0):
        return start
    return gen(las(start), n-1)

digits = int(math.log10(gen(1,30)))+1

print(digits)




