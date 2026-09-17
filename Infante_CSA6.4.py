
try:
    examscore = int(input("Enter your Examination Score: "))
    if 0 <= examscore <= 100:
        print("Valid Score.")
    else:
        print("Invalid Score.")

except ValueError:
    print("Invalid input. Please enter a number.")