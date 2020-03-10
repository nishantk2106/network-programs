import urllib.request

fhand =urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for lines in fhand :
    print(lines.decode().strip())

