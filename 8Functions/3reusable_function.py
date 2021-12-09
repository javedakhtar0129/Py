# just creating function to handle emoji conversion
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "ð",
        ":(": "ð"
    }
    output = ""
    for i in words:
        output += emojis.get(i,i) + " "

    return output


message = input("-->")
print(emoji_converter(message))
