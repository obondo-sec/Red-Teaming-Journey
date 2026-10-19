 Day 03 - Linux CLI & HTTP Fundamentals

**Theme:** Networking + Linux
**Date:** Mon 19 oct
**Time Spent:** [e.g., 4 Hours]

 🎯 Objective
Build muscle memory for the Linux command line using OverTheWire Bandit, and understand the fundamentals of HTTP Requests and Responses via TryHackMe.

 🛠️ Tools Used
- OverTheWire Bandit (Levels 1-6)
- TryHackMe (HTTP Requests & Responses room)
- Linux Terminal (Parrot OS)

 🧪 Lab Walkthrough
 1. OverTheWire Bandit (Levels 1-6)
Learned how to navigate the Linux file system via SSH. Key challenges included:
- Reading files with special characters in their names (Levels 1-2).
- Finding hidden files (Level 3).
- Using the `file` command to identify human-readable data (Level 4).
- Using the `find` command to locate files based on specific attributes (size, executable permissions) (Levels 5-6).

 2. TryHackMe: HTTP Requests & Responses
- Learned how a web browser communicates with a web server.
- Practiced using Browser DevTools (Network tab) to inspect traffic.
- Analyzed HTTP Methods (GET vs. POST).
- Learned how HTTP Status Codes work (200 OK, 302 Found/Redirect, 404 Not Found, 500 Internal Server Error).

 💻 Commands Learned
```bash
 Bandit Commands
find . -type f -size 1033c     Finds a file of exactly 1033 bytes
file ./*                       Checks the file type of all files in a directory

 HTTP Status Codes
 200 = OK
 302 = Redirect
 403 = Forbidden
 404 = Not Found



