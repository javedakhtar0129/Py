phone = input("Enter your mobile number: ")
digits_mapping = {
    1:"One","2":"Two","3":"Three","4":"Four",
    "5":"Five","6":"Six","7":"Seven","8":"Eight",
    "9":"Nine"
}
# making an empty output string

# looping through the string
outputS = ""
for ch in phone:
    outputS += digits_mapping.get(ch, "!!")+ " "

print(outputS)