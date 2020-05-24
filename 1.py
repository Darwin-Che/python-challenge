def myf(c):
    if ord(c)<97 or ord(c)>122 : return c
    if ord(c)==121 or ord(c) == 122 : return chr(ord(c)+2-26)
    return chr(ord(str(c))+2)

def f(l):
    z = str.maketrans("abcdefghijklmnopqrstuvwxyz",
                      "cdefghijklmnopqrstuvwxyzab")
    x = ""
    for c in l:
        x += c.translate(z)
    return x
t = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
t = "map"
q=map(myf,list(t))
print("".join(q))