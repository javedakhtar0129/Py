'''
1. We do manipulation of files by creating obects, these objects basically take
   refrence of file and sit in RAM to do processes in the file.
2. to pass directory address of file we use r before  open(r"C/python/filename.txt")
3.
w=write;r=read;a=appending;r+ =both read/write

'''

f = open("MyData.txt", "r")  # here f is the file object

#print(f.read())
print(f.readline())
print(f.readline())
print(f.readlines())  #It will create a list for us

print("-------")
