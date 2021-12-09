f = open("4list.txt","w")
# write lines takes a list and will put each element as a line
intro = ["my name is XYZ\n","I am T years old\n", "I like pancakes"]
f.writelines(intro)