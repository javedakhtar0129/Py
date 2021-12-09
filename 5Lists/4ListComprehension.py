# Below is one method of doing it
fruits = ["apple", "Banana", "Chiku", "Kiwi", "Watermelon"]
newlist1 = []
for x in fruits:
    if "a" in x:
        newlist1.append(x)
print(newlist1)

# Below is another method called list comprehension
newlist2 = [x for x in fruits if "a" in x]
newlist3 = ['A' for x in fruits if "a" in x] # this will print
print(newlist2)
print(newlist3)