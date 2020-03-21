# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the
# document from a URL, (2) displaying up to 3000 characters, and (3) counting the
# overall number of characters in the document. Don’t worry about the headers for
# this exercise, simply show the first 3000 characters of the document contents.


import urllib.request,urllib.parse,urllib.error
sum=0
file=urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt')
data=list()
for lines in file:
    data+=lines.decode().split()

for i in data:
    for j in i:
        sum=sum+1
        if(sum<=3000):print(j,sum)
        else:break
