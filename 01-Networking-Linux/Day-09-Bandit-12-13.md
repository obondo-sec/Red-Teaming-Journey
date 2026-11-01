 Day 09 - OverTheWire Bandit (Levels 12-13)

**Theme:** Networking + Linux
**Date:** [01 nov 2026]
**Time Spent:** [2.5 hours]

 🎯 Objective
Master file decompression techniques to reverse a heavily compressed file, and learn how to authenticate using SSH private keys.

 🛠️ Tools Used
- OverTheWire Bandit (Levels 12-13)
- Linux Terminal (Parrot OS)
- SSH, `file`, `xxd`, `gzip`, `bzip2`, `tar`

 🧪 Lab Walkthrough
1. **Level 12 (File Decompression):** 
   - Copied the data file to a writable directory (`/tmp`).
   - Used `file` to identify the file type (it was a hexdump).
   - Used `xxd -r` to reverse the hexdump back into a binary file.
   - Repeatedly used `file` to identify the next compression type and decompressed it using `gzip -d`, `bzip2 -d`, and `tar -xf` until the final text file was revealed.
2. **Level 13 (SSH Private Key):**
   - Found an SSH private key (`sshkey.private`).
   - Used `ssh -i sshkey.private bandit14@localhost -p 2220` to log in as the next user without needing a password.

 💻 Commands Learned
```bash
 Level 12: File manipulation and decompression
mkdir /tmp/myworkdir
cp data.txt /tmp/myworkdir
cd /tmp/myworkdir
file data.txt
xxd -r data.txt > data2.bin
file data2.bin
gzip -d data2.bin.gz
 (Repeated file and decompression steps for bzip2 and tar)

 Level 13: SSH with private key
ssh -i sshkey.private bandit14@localhost -p 2220
