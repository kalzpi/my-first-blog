import urllib.request
import pickle

request_url = 'http://www.pythonchallenge.com/pc/def/banner.p'

a = urllib.request
banner = a.urlopen(request_url)
data = pickle.load(banner)

for i in data:
    for j in i:
        text = j[0]
        times = j[1]
        k = 0
        while k < times:
            print(text, end='')
            k += 1
    print()

