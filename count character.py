# Change your socket program so that it counts the number of characters
# it has received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of
# characters and display the count of the number of characters at the end of the
# document.
import socket
sum=0
count=0
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org',80))
fhand=open('cover1.jpg','wb')
cmd='GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)
while True:
    data=mysocket.recv(3000)
    if(len(data)>3000 or len(data)<2):break
    count=count+1
    sum=sum+len(data)
    print(sum,len(data))
    fhand.write(data)
print("total copied items :",sum)
mysocket.close()


