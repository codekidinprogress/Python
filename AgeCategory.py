age = int(input("Enter your age: ")) # Asking user to enter age and converting it to integer (type casting)

if age < 0: # Age is negative, not possible in real life
    print("Age Cannot be Negative!")

elif 0 <= age <= 12:
    print("You are a Kid.")

elif 13 <= age <= 19:
    print("You are a Teenager.")

elif 20 <= age <= 35:
    print("You are a Young Adult.")

elif 36 <= age <= 59:
    print("You are an Adult.")

else:
    print("You are a Senior Citizen.")
