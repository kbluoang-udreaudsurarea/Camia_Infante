onlypaymethod = ["cash", "gcash", "card"]

paymethod = input("Enter your payment method: ").lower

if paymethod in onlypaymethod:
    print("Valid payment method.")

else:
    print("Invalid payment method.")