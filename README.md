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

Example:

```bash
python dns_lookup.py
```

or

```bash
python password_strength.py
```

## Disclaimer ⚠️

These tools are built for educational purposes and ethical security research only. Do not use them against systems you do not own or have permission to test.

## License
This project is licensed under the MIT License.

This project is licensed under the MIT License.
