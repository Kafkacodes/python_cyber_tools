# Python Cyber Tools

A collection of beginner-friendly Python tools for cybersecurity, networking, and automation.

## Features

### Password Strength Checker

* Checks password strength based on:

  * Length
  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters
* Provides strength ratings and feedback.

### Random Password Generator

* Generates secure random passwords.
* Supports customizable password length.
* Uses Python's secure random functions.

### File Metadata Viewer

* Displays file information such as:

  * File size
  * Creation time
  * Modification time
  * File extension
  * File or directory type

### Log Analyzer

* Reads log files and extracts useful information.
* Can be extended to detect errors, warnings, or suspicious activity.

### DNS Lookup Tool

Perform DNS and network lookups for domains and IP addresses.

Features:

* Domain → IP lookup
* IP → Domain lookup (Reverse DNS)
* Displays hostname information
* Lists common service ports
* Shows IPv4 and IPv6 addresses
* WHOIS lookup support

### Port Scanner

Scan TCP ports on domains or IP addresses and identify available services.

Features:

* Common Port Scanner
* Custom Port Scanner
* Service Detection
* Banner Grabbing
* Domain to IP Resolution
* Scan Timing
* Fast socket-based scanning
* Support for user-defined port lists

## Installation

Clone the repository:

```bash
git clone https://github.com/Kafkacodes/python_cyber_tools.git
cd python_cyber_tools
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

```bash
pip install python-whois
```

## Run a Tool

Examples:

```bash
python password_strength.py
python password_random.py
python meta_data.py
python log_analyzer.py
python dns_lookup.py
python port_scanner.py
```


## Future Improvements

* Multi-threaded Port Scanner
* UDP Scanning
* Latency Measurement
* Result Exporting
* HTTP Header Viewer
* Packet Analysis Utilities
* Network Reconnaissance Tools

## Disclaimer ⚠️

These tools are built for educational purposes and ethical security research only. Do not use them against systems you do not own or have permission to test.

## License

This project is licensed under the MIT License.
