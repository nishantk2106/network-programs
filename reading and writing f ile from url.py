import urllib.request,urllib.error,urllib.parse

img=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand=open('cover2.jpg','wb')
count=0
while True:
    info=img.read(100000)
    if len(info)<1:break
    count=count+len(info)
    fhand.write(info)

print(count,"character copied")
fhand.close()
