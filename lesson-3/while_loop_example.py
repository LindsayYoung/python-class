# example of while loop

# take input from the user
someInput = raw_input("type 3 to continue anything else to quit")

while someInput == '3':
    print("thank you for the 3, It was very kind of you")
    print("type 3 to continue, anything else to quit")
    someInput = raw_input()

print("How dare you, that is not a 3, I QUIT!")
