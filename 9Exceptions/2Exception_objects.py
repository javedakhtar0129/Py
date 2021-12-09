'''
If you dont know the what exception might occur then you can
also store an exception in a variable
'''
a= 5
b =0
try:
    print("--Resource open--")
    c=a/b

except Exception as e:  # you can put this at the last of all exception you know
    print("Hey, you cannont divide by zero,\n"
          "Some error has occured: ",e)
finally:
    print("--Resource Closed--")
    print("This is final statement,it'll print anyway")
