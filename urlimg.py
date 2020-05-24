import requests
from requests.auth import HTTPBasicAuth
import re

class urlimg:
    def __init__(self, urlstr, usrname, password):
        self.url = urlstr
        self.usr = usrname
        self.passwd = password
    def urlopen(self):
        return requests.get(self.url, auth=HTTPBasicAuth(self.usr, self.passwd))
    def disptxt(self):
        print(self.urlopen().text)
    def allimg(self):
        for i in re.findall('img .*?src="(.*?)"', self.urlopen().text):
            print(i)
    def dimg(self, n):
        name = re.findall('img .*?src="(.*?)"', self.urlopen().text)[n]
        img = urlimg(self.url.rsplit("/", 1)[0] + '/' + name, self.usr, self.passwd)
        print(img.url)
        with open(name, 'wb') as f:
            f.write(img.urlopen().content)
