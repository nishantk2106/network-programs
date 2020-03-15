import urllib.request
d=dict()
c=0
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt')
for lines in fhand:
    words=lines.decode().split()
    for word in words:
        if word not in d:
            d[word]=1
            c=c+1
        else:d[word]+=1

print("Total count of unique words in the url is ",c)


