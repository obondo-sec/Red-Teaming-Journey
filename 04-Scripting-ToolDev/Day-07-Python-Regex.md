 🧪 Advanced Regex (Pages 152-164)
Expanded my Regex knowledge by reading further into Chapter 7. Key concepts mastered:

1. **The Wildcard (`.`):** Matches any single character except a newline.
2. **The `*` and `+` Quantifiers:**
   - `*` matches zero or more occurrences.
   - `+` matches one or more occurrences.
3. **Character C
lasses (`[]`):** Matching specific sets of characters (e.g., `[aeiou]` for vowels).
4. **Negation (`[^...]`):** Matching anything *except* the characters inside the brackets.
5. **The `sub()` Method:** Using `re.sub()` to find a pattern and replace it with new text.
6. **Greedy vs. Non-Greedy Matching:** Using `.*?` to stop matching at the first occurrence rather than the last.

 💻 Advanced Script Example
```python
import re

 Example 1: Using the + quantifier (one or more)
 Matches 'S' followed by one or more 'p's (e.g., Sp, Spp, Sppp)
regex = re.compile(r'Sp+')
print(regex.search('The Sppp is large.').group()) # Output: Sppp

 Example 2: Using sub() to redact sensitive data
text = "My secret API key is ABC-123-XYZ."
 Replace any 3-letter, 3-number, 3-letter format with [REDACTED]
redacted = re.sub(r'[A-Z]{3}-\d{3}-[A-Z]{3}', '[REDACTED]', text)
print(redacted) # Output: My secret API key is [REDACTED].
