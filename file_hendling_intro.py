df=open("file.txt","r")
content=df.read()
print(content)
#here we are opening the file in read mode and then reading the content of the file and printing it.





with open('file.txt','w') as file:
    file.write("this line will be written to the file by the write method/n")
    file.write("this line will also be written to the file by the write method/n")
print("file has been written successfully")


