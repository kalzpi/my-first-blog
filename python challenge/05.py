import urllib.request, re

numb = '63579'
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'


a = urllib.request
p = re.compile('\d+')

while True:
    try:
        next = a.urlopen(url%numb).read().decode()
        numb = p.search(next).group()
        print(next)
    except:
        break

print(url)
print(numb)

#answer is http://www.pythonchallenge.com/pc/def/peak.html
