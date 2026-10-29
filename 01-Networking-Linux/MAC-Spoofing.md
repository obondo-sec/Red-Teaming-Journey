 MAC Address Spoofing (Native Linux)

**Theme:** Networking + Linux (OPSEC)
**Date:** [28 oct 2026]
**Time Spent:** [2 hours]

 🎯 Objective
Learn what a MAC address is and how to change it natively using the Linux `ip` command to bypass network filters and maintain OPSEC.

 🛠️ Tools Used
- Linux Terminal (Parrot OS)
- Native `ip` command
- `ifconfig` / `ip a`

 🧪 Lab Walkthrough
1. **Identify the Interface:** Used `ip a` to find my network interface name (e.g., `eth0` or `wlan0`) and noted the current MAC address.
2. **Take Down the Interface:** Brought the interface down using `sudo ip link set dev [interface] down`.
3. **Change the MAC:** Used the `ip link` command to manually assign a new MAC address.
4. **Bring the Interface Up:** Brought it back online using `sudo ip link set dev [interface] up`.
5. **Verify:** Ran `ip a` again to confirm the MAC address had successfully changed.

 💻 Commands Used
```bash
 1. View current MAC address
ip a

 2. Bring interface down (required before changing MAC)
sudo ip link set dev eth0 down

 3. Change to a specific MAC address (example)
sudo ip link set dev eth0 address 00:11:22:33:44:55

 4. Bring interface up
sudo ip link set dev eth0 up

 5. Verify the change
ip a
