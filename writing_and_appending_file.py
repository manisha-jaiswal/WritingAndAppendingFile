f=open("manu2.txt","w") #file name and file mode,it replace the file content and replace in new content
f.write("I am very cute\n")
f.close()
f=open("manu.txt","a")
a=f.write("I am so beautiful \n ")
print(a)
f.close

#read and write mode
f=open("manu2.txt","r+")
print(f.read())
f.write("thanku")
f.close()


#tell and seek function
f=open("manu2.txt")
#print(f.tell()) #tell is used for finding the position of file pointer

print(f.readline())
#print(f.tell())
print(f.seek(10)) #seek is used for reading the file using the particuler length which is given by user,here it starts with 10
print(f.readline())
#print(f.tell())
#print(f.readline())
f.close()