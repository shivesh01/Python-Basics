f=open("hello.txt",'r',encoding='utf=8')
print(f.read(4))
print(f.read(4))
print('\n',f.read(),'\n')
print(f.tell())             #curson position in number of bytes
print(f.seek(0))            #cursor intial position
print(f.readline())
print(f.readline())#read text line by line
f.close()
print("file closed")
