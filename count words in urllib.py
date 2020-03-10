import urllib.request
d=dict()
lst=list()
c=0
fhand=urllib.request.urlopen('http://r-statistics.co/Linear-Regression.html')
for lines in fhand:
    words=lines.decode().split()
    for word in words:
        if word not in d:
            d[word]=1
            c=c+1
        else:d[word]+=1

print("Total count of words in the url is ",c)


