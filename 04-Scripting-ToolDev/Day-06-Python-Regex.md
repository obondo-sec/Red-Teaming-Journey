 Day 06 - Python Pattern Matching (Regex)

**Theme:** Scripting + Tool Dev
**Date:** [25 oct 2026]
**Time Spent:** [ 1.5 Hours]

 🎯 Objective
Learn how to use Python's `re` module for pattern matching and text extraction by reading Chapter 7 (pages 147-153) of "Automate the Boring Stuff with Python".

 🛠️ Tools Used
- Python 3
- `re` module (Regular Expressions)
-  Terminal

 🧪 Concepts Learned
1. **Regular Expressions (Regex):** A powerful way to search for specific patterns in text.
2. **The `re` module:** Importing `import re` and using `re.compile()` to create Regex objects.
3. **Matching:** Using `search()`.
4. **Character Classes:** Using `\d` (digits)
5. **Groups:** Using parentheses `()` to group parts of the pattern together.
 💻 Scripts / Code Written
```python
import re

... Example: Extracting all phone numbers from a text
text = "Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office."  				
 The regex pattern for a US phone number: 3 digits, dash, 3 digits, dash, 4 digits
phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
matches = phone_regex.findall(text)

print(f"Found phone numbers: {matches}")


