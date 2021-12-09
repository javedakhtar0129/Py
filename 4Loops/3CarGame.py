command = ""
started = False
stopped = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started == True:
            print("Car is already started")
        else:
            print("Car started...")
            started = True
            stopped = False
    elif command == "stop":
        if stopped == True:
            print("Car is already stopped")
        else:
            print("Car stopped")
            stopped = True
            started = False
    elif command == "help":
        print('''
start- to start the car
stop - to stop the car
quit - to quit the program
help - to ask for help''')
    elif command == "quit":
        print("Prog ended!!")
    elif command == "quit":
        break
    else:
        print("I didn't get it")
