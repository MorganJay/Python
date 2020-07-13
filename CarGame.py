gameHelp = """type start - to start the car
type stop - to stop the car
type quit - to exit the game"""
userCommand = ""
started = False
stopped = False
# while userCommand != "quit":
while True:
    userCommand = input("> ").lower()
    if userCommand == "start":
        if started:
            print("Please enter your car is running")
        else:
            started = True
            print("Car started...Ready to go!")
    elif userCommand == "stop":
        if not started:
            print("Please start the car first oga")
        else:
            started = False
            print("Car stopped.")
    elif userCommand == "help":
        print(gameHelp)
    elif userCommand == "quit":
        break
    else:
        print("I don't understand that, type help")
