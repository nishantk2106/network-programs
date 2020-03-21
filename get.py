import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/romeo-full.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data=mysock.recv(512)
    if(len(data)<2):break
    data=data.decode()
    y=data.find('\r\n\r\n')
    print(data[368:])
mysock.close()


