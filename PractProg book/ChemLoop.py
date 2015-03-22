__author__ = 'Ryan'
text = " "
while text != "quit":
    text = input("Please enter a chemical ( or 'quit' to exit): ")
    if text == "quit":
        print("exiting program")
        break
    elif text == "H20":
        print("water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("You suck")
