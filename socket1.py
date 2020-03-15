import socket
x=input("Enter the URL :")
a=str()
y=int(input("Enter the port number :"))
x=x.split('/')
x=x[2]
print(x)
try:
      mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      mysock.connect((x,y))
except:
     print("Could not find the URL")
     exit()
