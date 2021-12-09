sentence = "This is basic sentence"
print(len(sentence))  #len gives the length of the string

print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
# find method is case sensitive
print(sentence.find('T'))
print(sentence.find('Thi'))
print(sentence.find('ic se'))

print(sentence.replace('basic','Advance'))

print('basic' in sentence)  # in operator produces a boolean value







