message = input(">")
#It will split the string wherever it finds "x"..
# ..and stores it in a list as separate words
word = message.split(" ") #spliting at whitespaces
print(word)
#Now we map our emojis
emoji = {
    ":)":"ð",
    ":(":"ð"
}
outp = ""
for i in word:
    outp += emoji.get(i,i) + " "

print(outp)
