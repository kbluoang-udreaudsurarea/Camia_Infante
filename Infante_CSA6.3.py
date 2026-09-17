

pin = input("Enter a 4-DIGIT PIN: ")

if len(pin) == 6 and pin.isdigit():
    print("Valid PIN.")

else:
    print("Invalid PIN. Enter exactly 6 digits.")