import socket
import sys

# Ask the user for a website or IP to scan
target = input("Enter the target host (e.g., google.com or 192.168.1.1): ")

# Translate hostname to IP
try:
    ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Error: Hostname could not be resolved.")
    exit()

print(f"\nStarting scan on {ip}...\n")

# Spinner characters
spinner = ['|', '/', '-', '\\']

# Loop through port numbers 1 to 100
for port in range(1, 101):
    # Show rotating slash
    sys.stdout.write(f"\rScanning port {port} {spinner[port % 4]}")
    sys.stdout.flush()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"\nPort {port} is OPEN")
    s.close()
print("\n\nScan completed.")
