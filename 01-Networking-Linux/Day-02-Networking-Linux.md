# Day  1 - Networking & Linux Fundamentals

**Theme:** Networking + Linux
**Date:** October 15, 2026
**Time Spent:** 2 Hours

## 🎯 Objective
Understand the TCP/IP model, master Linux file permissions (`chmod`, `chown`), and learn how to search text using `grep`.

## 🛠️ Tools Used
- Professor Messer (TCP/IP videos)
- Parrot OS Terminal

## 🧠 Theory Notes
- **TCP/IP Model:** 4 layers (Link, Internet, Transport, Application).
- **TCP vs UDP:** TCP is reliable (3-way handshake), UDP is fast (no handshake).
- **Linux Permissions:** `chmod 755` = `rwxr-xr-x`. `chown` changes file owner and group.

## 💻 Commands Learned
```bash
chmod 755 script.sh        # Sets rwxr-xr-x permissions
chown user:group file.txt  # Changes file owner and group
grep "root" /etc/passwd    # Searches for the string "root" in a file
