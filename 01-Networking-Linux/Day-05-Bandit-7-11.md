 Day 05 - OverTheWire Bandit (Levels 7-11)

**Theme:** Networking + Linux
**Date:** [Thu 22 oct]
**Time Spent:** [ 2 Hours]

 🎯 Objective
Advance Linux command-line skills by finding hidden data, filtering text, decoding base64, and using basic ciphers in OverTheWire Bandit.

 🛠️ Tools Used
- OverTheWire Bandit (Levels 7-11)
- Linux Terminal (Parrot OS)

 🧪 Lab Walkthrough
1. **Level 7:** Used `grep` to search for a specific word inside a massive text file (`data.txt`).
2. **Level 8:** Found a line of text that appeared only once in the file by combining `sort` and `uniq -u`.
3. **Level 9:** Used the `strings` command to extract human-readable text from a binary file, then piped it to `grep` to find the password preceded by `=`.
4. **Level 10:** Identified base64 encoded data and decoded it using the `base64 -d` command.
5. **Level 11:** Identified ROT13 encoded text and used the `tr` command to translate the characters and reveal the password.

 💻 Commands Learned
```bash
# Level 7: Search for a string in a file
grep "millionth" data.txt

 Level 8: Find unique lines
sort data.txt | uniq -u

 Level 9: Extract readable strings and find specific characters
strings data.txt | grep "==="

 Level 10: Decode base64
base64 -d data.txt

 Level 11: ROT13 translation
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
