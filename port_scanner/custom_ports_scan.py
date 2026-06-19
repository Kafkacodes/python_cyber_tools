domain = input("Enter a domain name or IP address: ").strip()
import socket
import time

start = time.time()
ports = input("Enter the ports you want to scan (comma-separated): ")
ports = [int(p.strip()) for p in ports.split(",")]

ip = socket.gethostbyname(domain)
print(f"Scanning {domain}\n ({ip})...")

for port in ports:
    s = socket.socket()
    s.settimeout(0.05)

    try:
        name = socket.getservbyport(port)
    except OSError:
        name = "Unknown"
    if s.connect_ex((ip, port)) == 0:
        print(f"[OPEN] Port {port} ({name})")

        try:
            banner = s.recv(1024).decode().strip()
            if banner:
                print(f"Banner: {banner}")
        except:
            print("No banner received.")
    s.close()   

end = time.time()
print(f"\nScan completed in {end - start:.2f} seconds.")