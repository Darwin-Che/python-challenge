import urllib.request
import pickle

fp = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")

t = pickle.load(fp)

print(t)

# for lines in t:
#     for tu in lines:
#         for i in range(tu[1]):
#             print(tu[0], end = '')
#     print("\n")
