print("Recipient Name")
# Please fill in recipient's name in ("") below
recipient_name = input()

print("Current year")
# Please fill in the current year in () below, eg: 2023
current_year = int(input())

print("Year of Birth")
# Please fill in the year of birth in () below, eg: 1999
yob = int(input())

age = (current_year - yob)

print("Message")
# Please fill in the Short Personalized Message in ("") below
message = input()

print("Sender Name")
# Please fill in the sender name in ("") below
sender_name = input()
print("\n\n")

# Final outcome
print(f"{recipient_name}, let's celebrate your {age} years of awesomeness!\nWishing you a day filled with joy and laughter as you turn {age} !\n\n")
print(f"{message}\n\n")
print(f"With love and best wishes,\n{sender_name}")

input()





