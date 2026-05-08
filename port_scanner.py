import socket
from datetime import datetime

print("=" * 50)
print("        TCP PORT SCANNER")
print("=" * 50)

# Take target IP
host = input("Enter target IP or website: ")

# Convert website to IP
try:
    target_ip = socket.gethostbyname(host)
except:
    print("Invalid host")
    exit()

print(f"\nScanning Target: {target_ip}")
print(f"Scan Started At: {datetime.now()}")
print("-" * 50)

# File to save results
file = open("scan_results.txt", "w")
file.write(f"Port Scan Results for {target_ip}\n")
file.write("-" * 50 + "\n")

# Common ports
ports = [20,21,22,23,25,53,80,110,135,139,143,443,445,3306,8080]

for port in ports:
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target_ip, port))

    if result == 0: 
        print(f"[OPEN] Port {port}")
        file.write(f"[OPEN] Port {port}\n")
    else:
        print(f"[CLOSED] Port {port}")

    scanner.close()

print("\nScan Completed")
file.close()