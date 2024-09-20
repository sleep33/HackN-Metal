
# HackN’Metal - Pentesting Like a Metalhead

```
 _    _            _     _   _      __  __      _        _ 
| |  | |          (_)   | | | |    |  \/  |    | |      | |
| |__| | __ _ _ __ _ ___| |_| | ___| \  / | ___| |_ __ _| |
|  __  |/ _` | '__| / __| __| |/ _ \ |\/| |/ _ \ __/ _` | |
| |  | | (_| | |  | \__ \ |_| |  __/ |  | |  __/ || (_| | |
|_|  |_|\__,_|_|  |_|___/\__|_|\___|_|  |_|\___|\__\__,_|_|
----------------------------------------------------------

## What is HackN’Metal?
**HackN’Metal** is a badass pentesting tool for lazy hackers who live and breathe metal. It automates reconnaissance, port scanning, enumeration, vulnerability scanning, and exploitation while spitting out some heavy, no-nonsense metal-flavored commentary.

## Features:
- **Reconnaissance**: Dig deep into target info.
- **Port Scanning**: Scan ports like a Meshuggah riff.
- **Enumeration**: Identify services and users in the target network.
- **Vulnerability Scanning**: Hunt for weak spots in the system.
- **Exploitation**: Time to break things and take control!

## Installation Guide

### 1. Prerequisites
Before you begin, you need to have Python 3 installed along with some basic pentesting tools like `nmap`, `whois`, `enum4linux`, and `metasploit`. Follow the instructions below for your OS.

### 2. Install on Linux (Debian-based distros like Ubuntu)

1. **Update and install the required tools**:
   ```bash
   sudo apt-get update
   sudo apt-get install -y python3 python3-pip whois nmap enum4linux metasploit-framework
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/hacknmetal.git
   cd hacknmetal
   ```

3. **Run the script**:
   ```bash
   python3 hacknmetal.py
   ```

### 3. Install on macOS

1. **Install Homebrew** (if you don't have it already):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install the required tools**:
   ```bash
   brew install python3 nmap whois
   brew install --cask metasploit
   ```

3. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/hacknmetal.git
   cd hacknmetal
   ```

4. **Run the script**:
   ```bash
   python3 hacknmetal.py
   ```

### 4. Install on Windows

1. **Install Python**: 
   - Download and install Python 3.x from the official site: [Python Download](https://www.python.org/downloads/)
   - Make sure to check the box **"Add Python to PATH"** during installation.

2. **Install the required tools**:
   - Download and install **Nmap**: [Nmap for Windows](https://nmap.org/download.html#windows)
   - Install **Metasploit**: [Metasploit for Windows](https://windows.metasploit.com/)
   - Use **Windows Subsystem for Linux (WSL)** to install **whois** and **enum4linux**:
     1. Open PowerShell as Administrator and run:
        ```powershell
        wsl --install
        ```
     2. Inside the WSL terminal (after it's installed), run:
        ```bash
        sudo apt-get install whois enum4linux
        ```

3. **Clone the repository**:
   - Open PowerShell or Command Prompt and run:
     ```powershell
     git clone https://github.com/yourusername/hacknmetal.git
     cd hacknmetal
     ```

4. **Run the script**:
   ```powershell
   python hacknmetal.py
   ```

## Usage Instructions

1. Run the tool by executing:
   ```bash
   python3 hacknmetal.py
   ```

2. You will see a menu with the following options:
   ```
   -----------------------------------
    HackN’Metal — Hacking with Attitude!
   -----------------------------------
   1. Reconnaissance (Dig Deep Like a Heavy Bassline)
   2. Scanning (Ports are gonna tremble)
   3. Enumeration (Find who’s playing what in this network jam)
   4. Vulnerability Scanning (Someone here is weak as f***)
   5. Exploitation (It’s time to destroy!)
   6. Run All Tests (Cause you don’t have time for bullshit)
   7. Exit and go blast some f***ing metal!
   -----------------------------------
   Your move, badass. Pick something [1-7]:
   ```

3. Choose an option and follow the prompts to enter the target.

-------------------------------------------------------
                Created with chaos by sleep33
-------------------------------------------------------
