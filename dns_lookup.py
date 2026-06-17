import socket

choice = input("1. Lookup domain info from domain name\n2. Reverse DNS lookup\nEnter your choice (1 or 2): ").strip()

if choice == "1":
    domain = input("Enter a domain name: ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"\nThe IP address of {domain} is: {ip}")

    except:
        print(f"this {domain} is not a valid domain name.")

    host = socket.getfqdn(domain)
    print(f"host name of {domain} is: {host}\n")

    services = ["ftp", "http", "https", "smtp", "pop3", "imap", "domain", "ssh", "telnet"]
    for service in services:
        try:
            port = socket.getservbyname(service)
            print(f"{service} runs on port: {port}")
        except:
            print(f"{service} is not a valid service name.")

    address = socket.getaddrinfo(domain, None)

    ips = set()
    for adrr in address:
        ips.add(adrr[4][0])

    print("\nAll IP Addresses:")
    for ip in ips:
        if ":" in ip:
            print(f"IPv6: {ip}")
        else:
            print(f"IPv4: {ip}")

elif choice == "2":
    ip_address = input("Enter an IP address: ")
    try:
        domain_name = socket.gethostbyaddr(ip_address)
        print(f"\nThe domain name for IP address {ip_address} is: {domain_name[0]}")
    except:
        print(f"this {ip_address} is not a valid IP address.")
    
else:
    print("Invalid choice. Please enter 1 or 2")