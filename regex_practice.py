import re 
phone_regex = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
#mo = phone_regex.search("My number is 122-555-4242")
#if mo:
	#print("Number Found:" + mo.group())
#else:
	#print("Number not found")
#print(mo.group(1))
#print(mo.group(2))
#print(mo.group(3))
#print(mo.group(0))

# 1. Define the regex pattern (allowing optional area code)

# 2. Ask the user for input
user_input = input("Please enter your phone number: ")

# 3. Verify the input using fullmatch
if phone_regex.fullmatch(user_input):
    print(" Success! That is a valid phone number.")
else:
    print(" Error: Invalid format. Please use '000-000' or '000-000-0000'.")
