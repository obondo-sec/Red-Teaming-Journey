import re 
phone_regex = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
mo = phone_regex.search("My number is 122-555-4242")
#if mo:
	#print("Number Found:" + mo.group())
#else:
	#print("Number not found")
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))
print(mo.group(0))
