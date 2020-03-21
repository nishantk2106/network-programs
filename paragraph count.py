# Exercise 4: Change the urllinks.py program to extract and count paragraph (p)
# tags from the retrieved HTML document and display the count of the paragraphs
# as the output of your program. Do not display the paragraph text, only count
# them.
import urllib.request,urllib.parse,urllib.error
file=urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt')
paracount=1
for line in file:
    data=line.split()
    if data==[]:paracount=paracount+1

print(paracount)


