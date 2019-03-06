import zipfile, urllib.request, os, re

url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
zipped_binary = urllib.request.urlopen(url).read()

if not os.path.exists('channel.zip'):   #만약 최상위 경로에 channel.zip 파일이 없다면
    fp = open('channel.zip', 'wb')      #최상위 경로에 channel.zip 파일을 쓰기+바이너리
    fp.write(zipped_binary)             #fp 안에 zipped_binary data를 입력
    fp.close()

file_numb = '90052'

##zipfile은 그냥 패스하자 잘 모르겠다