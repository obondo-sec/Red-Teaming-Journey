 Day 05 - Python Basics (TryHackMe)

**Theme:** Scripting + Tool Dev
**Date:** [Wed 21 oct]
**Time Spent:**  1 Hour]

 🎯 Objective
Complete the TryHackMe "Python Basics" room to build a foundation for writing custom Red Team tools and automating tasks.

 🛠️ Tools Used
- TryHackMeO
- Python 3
- Linux Terminal

 🧪 Lab Walkthrough
Completed the TryHackMe Python Basics room. Key concepts covered:
1. **Variables and Data Types:** Strings, Integers, Floats, Booleans.
2. **Control Flow:** `if`, `elif`, and `else` statements.
3. **Loops:** `for` loops and `while` loops.
4. **Functions:** Defining reusable blocks of code using `def`.
5. **Imports:** Using built-in modules like `os` and `sys`.

 💻 Scripts / Code Written
```python
 Example: A simple function to check if a port is likely open (mock scenario)
def check_port(port):
    if port == 80 or port == 443:
        return "Common Web Port"
    else:
        return "Other Port"

 Using a for loop to iterate through a list
ports_to_check = [22, 80, 443, 3306]
for port in ports_to_check:
    print(f"Port {port}: {check_port(port)}")

