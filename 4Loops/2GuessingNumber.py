'''
In python while loop also has a else statement
else statement runs when condition of while loop is no more true
'''

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count<guess_limit:
     guess = int(input("Guess a number: "))
     guess_count+=1
     if guess == secret_number:
         print("YOU WON!")
         break
else:
    print("You loose(This msg was on default else in while)")

if guess != secret_number:
    print("\nYou Loose!(This msg was on if statement I added after while loop)")

print("Done!")