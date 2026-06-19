domain = input("Enter a domain name or IP address: ").strip()
import socket
import time
start = time.time()

common_ports = common_ports = [
    21, 22, 23, 25, 53,
    80, 110, 135, 139, 143,
    443, 445,
    993, 995,
    1433, 3306,
    3389, 5432,
    5900, 6379,
    8080, 8443,
    9000, 9200,
    27017
]

print(f"\nScanning common ports for {domain}...\n")

for port in common_ports:
    s = socket.socket()
    s.settimeout(0.05)
    
    try:
        name = socket.getservbyport(port)
    except OSError:
        name = "Unknown"
    ip = socket.gethostbyname(domain)
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