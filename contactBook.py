contacts = {
    "Aman": "9876543210",
    "Riya": "9123456780",
    "Karan": "9998887776"
}

name = input("Enter a name: ")

if name in contacts:
    print(f"{name}'s number is {contacts[name]}")
else:
    print("Contact not found.")
