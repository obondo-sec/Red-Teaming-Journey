import re
import pyperclip
email_re = re.compile(r"([a-zA-Z0-9])+@([a-zA-Z]+)./[a-zA-Z]{2,4}")
phone_re = re.compile(r"(\+254|0)([17])\d{8}")
raw_text = pyperclip.paste()
cleaned_phone = raw_text.replace(" "," ")
found_phones = phone_re.findall(cleaned_phone)
found_emails = email_re.findall(raw_text)
print("===== RESULTS =====\n")
try:
    with open("emails_and_phone", "r") as file:
        raw_text = file.read()
except FileNotFoundError:
    print(" Error: File not found. Please check the name.")
    exit()
try:
	with open("emails_and_phone","r") as file:
		raw_text = file.read()
except FileNotFoundError:
	print("Error : File not found")
	exit()
	
