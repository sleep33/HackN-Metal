
# HackN'Metal - Pentesting Like a Metalhead
![Cover](https://github.com/user-attachments/assets/12bfe2c0-0242-43d4-95e5-a884c60358f8)

```
 _    _            _     _   _      __  __      _        _ 
| |  | |          (_)   | | | |    |  \/  |    | |      | |
| |__| | __ _ _ __ _ ___| |_| | ___| \  / | ___| |_ __ _| |
|  __  |/ _` | '__| / __| __| |/ _ \ |\/| |/ _ \ __/ _` | |
| |  | | (_| | |  | \__ \ |_| |  __/ |  | |  __/ || (_| | |
|_|  |_|\__,_|_|  |_|___/\__|_|\___|_|  |_|\___|\__\__,_|_|
----------------------------------------------------------
```

## Disclaimer:
**HackN'Metal** is designed for **research and educational purposes only**. This tool should only be used on systems that you own or have explicit permission to test. Unauthorized access to computer systems is illegal and unethical.

Use this tool responsibly and in compliance with all applicable laws and regulations.

## What is HackN'Metal?

**HackN’Metal** is a badass pentesting tool for lazy hackers who live and breathe metal. It automates reconnaissance, port scanning, enumeration, vulnerability scanning, and exploitation while spitting out some heavy, no-nonsense metal-flavored commentary.

## Features:
1. **Reconnaissance**: Perform a deep information gathering on the target.
2. **Port Scanning**: Scan open ports like a Meshuggah riff.
3. **Enumeration**: Discover network services, users, and other important details.
4. **Vulnerability Scanning**: Identify known vulnerabilities using Nmap scripts.
5. **Exploitation**: Execute automated exploit attempts using Metasploit.
6. **Run All Tests**: Perform all steps in one go without interaction.
7. **AI-Driven Recommendations**: Analyze scan results using AI to suggest next steps or known vulnerabilities (NEW).

## AI-Driven Recommendations

**AI-Driven Recommendations** is a powerful feature in **HackN'Metal** that provides actionable insights based on scan results.

### How it works:
- After performing a reconnaissance or port scan, the tool analyzes the scan results (e.g., services like Apache or MySQL).
- The AI will look for known vulnerabilities (CVE entries, Exploits) related to the identified services and their versions.
- It provides recommendations on what to do next, such as running an exploit or patching vulnerable services.

This feature helps users by automatically suggesting further actions and even specific known vulnerabilities that match the services found.

### Example Output:
```
[*] Found vulnerability in Apache 2.4.49: CVE-2021-41773
    Exploit for path traversal in Apache

[+] Further steps: Consider running an exploit or patching the vulnerable services.
```

## Installation

### Prerequisites:
- Python 3.x
- `nmap`
- `enum4linux`
- `msfconsole` (Metasploit Framework)

Make sure these tools are installed on your system.

### Installation Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hacknmetal.git
   cd hacknmetal
   ```

2. Install the necessary tools:
   ```bash
   # On Debian-based systems (e.g., Ubuntu):
   sudo apt-get install python3 nmap enum4linux metasploit-framework
   ```

3. Run the script:
   ```bash
   python3 hacknmetal.py
   ```

## Usage

### Menu Options:
- **1. Reconnaissance**: Perform information gathering.
- **2. Scanning**: Scan open ports on the target.
- **3. Enumeration**: Identify services and users.
- **4. Vulnerability Scanning**: Identify potential vulnerabilities.
- **5. Exploitation**: Attempt to exploit identified vulnerabilities.
- **6. Run All Tests**: Run all the above steps in sequence.
- **7. AI-Driven Recommendations**: Get AI-based recommendations on further actions.
- **8. Exit**: Exit the tool and get back to your music.

### Example Workflow:

1. Run the tool:
   ```bash
   python3 hacknmetal.py
   ```

2. Choose an option from the menu, for example, **1. Reconnaissance**.

3. Input the target you want to scan:
   ```bash
   Enter the target to scan: 192.168.1.1
   ```

4. Let the tool do its magic, providing useful and humorous feedback.

5. To use **AI-Driven Recommendations**, choose **7** after performing reconnaissance. The AI will suggest vulnerabilities and potential next steps.

## License

This project is licensed under the MIT License.
