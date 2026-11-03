 Day 10 - Python Web Scraping & Requests (ABSWP Ch. 11)

**Theme:** Scripting + Tool Dev
**Date:** [NOV 3 2026]
**Time Spent:** [ 2 Hour]
 🎯 Objective
Learn how to automate web interactions using Python by reading Chapter 11 (pages 133-138) of "Automate the Boring Stuff with Python". Focus on the `webbrowser` and `requests` modules.

 🛠️ Tools Used
- Python 3
- `webbrowser` module (built-in)
- `requests` module (third-party)
- VS Code / Terminal

 🧪 Concepts Learned
1. **The `webbrowser` Module:** Using `webbrowser.open('https://example.com')` to automatically launch the default web browser to a specific URL.
2. **The `requests` Module:** Using `requests.get()` to programmatically download a web page or interact with an API without needing a browser.
3. **Status Codes:** Using `response.status_code` to check if the request was successful (e.g., `200` for OK, `404` for Not Found).
4. **Response Content:** Accessing the raw HTML of a page using `response.text`.

 💻 Scripts / Code Written
```python
import webbrowser
import requests

 Example 1: Open a browser automatically
 webbrowser.open('https://portswigger.net') 

 Example 2: Download a webpage using requests
url = 'http://example.com'
response = requests.get(url)

 Check if the request worked
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    print("Successfully downloaded the page!")
    # Print the first 200 characters of the HTML to verify
    print(response.text[:200])
else:
    print("Failed to download the page.")

 Example 3: Downloading a file (simulated)
 response = requests.get('https://example.com/some_file.txt')
 with open('downloaded_file.txt', 'wb') as file:
     file.write(response.content)
