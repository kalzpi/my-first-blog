import urllib.request, re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'


a = urllib.request
b = a.urlopen(url).read()

print(b)
print(type(b))

p = re.compile('\d+')

m = p.search(b.decode())

print(m.group())
print(type(m))

