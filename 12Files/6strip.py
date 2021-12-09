f = open("6strip.txt","w+")
f.write("aaadhvuvoaacha")
A = " aaHello today we will study  python.a "
B = "aaAEFSFFa"
# strip will strip away the string passed in it from start and end
print(B.strip("a"))
print(A.strip()) #if nothing is passed it means it'll delete whitespaces
print(B.lstrip("a")) #strip left side only
print(B.rstrip("a")) #strip right side only

# To remove \n delimiter from end of the line we use s=s.rstrip("\n")

