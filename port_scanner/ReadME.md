# Python Port Scanner

A beginner-friendly cybersecurity project built with Python that scans TCP ports on a target host and identifies common network services.

This project includes:

- Common Ports Scanner
- Custom Ports Scanner
- Service Detection
- Banner Grabbing
- Scan Timing

---

## Features

### Common Ports Scanner

Quickly scans a predefined list of commonly used ports:

- FTP (21)
- SSH (22)
- Telnet (23)
- SMTP (25)
- DNS (53)
- HTTP (80)
- POP3 (110)
- RPC (135)
- NetBIOS (139)
- IMAP (143)
- HTTPS (443)
- SMB (445)
- IMAPS (993)
- POP3S (995)
- MSSQL (1433)
- MySQL (3306)
- RDP (3389)
- PostgreSQL (5432)
- VNC (5900)
- Redis (6379)
- HTTP Alternate (8080)
- HTTPS Alternate (8443)
- SonarQube (9000)
- Elasticsearch (9200)
- MongoDB (27017)

---

### Custom Ports Scanner

Allows users to scan any ports they choose.

Example:

```text
80,443,8080,3306
```

---

### Service Detection

Attempts to identify the service running on an open port using Python's socket library.

Example:

```text
[OPEN] Port 22 (ssh)
[OPEN] Port 443 (https)
```

---

### Banner Grabbing

Attempts to retrieve service banners from open ports.

Example:

```text
[OPEN] Port 21 (ftp)

Banner:
220 FTP Server Ready
```

This helps identify software and service versions.

---

### Scan Timing

Measures how long the scan takes.

Example:

```text
Scan completed in 0.52 seconds.
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Kafkacodes/python_cyber_tools.git
cd python_cyber_tools
```

No external dependencies are required.

Python 3.10+ recommended.

---

## Usage

### Common Port Scanner

```bash
python port_scanner.py
```

Example:

```text
Enter a domain name or IP address: scanme.nmap.org
```

---

### Custom Port Scanner

```bash
python custom_ports_scan.py
```

Example:

```text
Enter a domain name or IP address: scanme.nmap.org

Enter the ports you want to scan (comma-separated):
21,22,80,443
```

---

## Example Output

```text
Scanning scanme.nmap.org
(45.33.32.156)...

[OPEN] Port 22 (ssh)
Banner: SSH-2.0-OpenSSH_9.2

[OPEN] Port 80 (http)

Scan completed in 0.47 seconds.
```


## Future Improvements

- Port Range Scanning (1-1024)
- Multi-threaded Scanning
- WHOIS Lookup
- Latency Measurement
- UDP Scanning
- Result Exporting
- Interactive Menu System
- Nmap-style Service Fingerprinting

---

## Disclaimer

This tool is intended for educational purposes and authorized testing only.

Only scan systems that you own or have explicit permission to test.
