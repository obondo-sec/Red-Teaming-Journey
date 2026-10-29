import re
import pyperclip
email_re = re.compile(r"([a-zA-Z0-9])+@([a-zA-Z]+)./[a-zA-Z]{2,4}")
phone_re = re.compile(r"(\+254|0)([17])\d{8}")
raw_text = pyperclip.paste()
cleaned_phone = raw_text.replace(" "," ")
found_phones = phone_re.findall(cleaned_phone)
found_emails = email_re.findall(raw_text)
print("===== RESULTS =====\n")
if found_phones:
	print(f"Found{len(found_phones)}Phone Number(s):")
	for phone in found_phones:
		full_number = "".join(phone)
		print(f" -{full_number}")
else: 
	print("No Phone Numbers  Found.")
print("\n")
if found_emails:
	print(f"found{len(found_emails)}Email(s):")
	for email in found_emails:
		print(f" - {email}")
else:
	print("No emails found.")
	
