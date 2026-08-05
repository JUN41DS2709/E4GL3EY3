import shutil
import sys
from modules.headers import headers_analysis
from modules.dns import dns_anlysis
from rich import print
from modules.whois_lookup import whois_analysis
from modules.cert import cert_analysis
from modules.robot import robot_analysis
from modules.tech import tech_analysis
def show_menu():
    columns ,_ = shutil.get_terminal_size(fallback=(80, 24))
    line,line1 =  "="*columns , "─"*columns
    print(line)
    text = "Main Menu"
    print(text.center(columns))
    print(line)

    print(line1)
    print("\n🌐Passive Domain Reconnaissance Framework\n")
    print(line1)
    print("MODULES INCLUDED \n")
    print("[1] Header Analysis      - Inspect HTTP response headers.")
    print("[2] DNS Record Analysis  - Passive DNS reconnaissance.")
    print("[3] WHOIS Analysis       - Retrieve domain registration information.")
    print("[4] SSL/TLS Certificate Analysis - Inspect SSL/TLS certificate details.")
    print("[5] Robots.txt Analysis  - Check for robots.txt file and its contents.")
    print("[6] Technology Stack Analysis - Identify technologies used by the target website.")

    print(line)
    print("Enter 1 to start scanning.....")
    print("Enter 0 or exit to quit the program.....")
    print(line)

    choices = int(input("$ Select an option > "))
    if choices == 1:
        target = input("$ Enter Target >  ")
        print(line)
        print(f"$ TARGET : {target}\n")
        print(line)

        print("Select Recon Type :- \n")
        print("[purple] [1] Header Analysis      - Inspect HTTP response headers.[/purple]")
        print("[purple] [2] DNS Record Analysis  - Passive DNS reconnaissance.[/purple]")
        print("[purple] [3] WHOIS Analysis       - Retrieve domain registration information.[/purple]")
        print("[purple] [4] SSL/TLS Certificate Analysis - Inspect SSL/TLS certificate details.[/purple]")
        print("[purple] [5] Robots.txt Analysis  - Check for robots.txt file and its contents.[/purple]")
        print("[purple] [6] Technology Stack Analysis - Identify technologies used by the target website.[/purple]")
        
        recon_type = int(input("Select type [1] , [2] , [3] , [4].. > "))
        match recon_type:
            case 1:
                headers_analysis(target)
            case 2:
                dns_anlysis(target)
            case 3:
                whois_analysis(target)
            case 4:
                cert_analysis(target)
            case 5:
                robot_analysis(target)
            case 6:
                tech_analysis(target)        
    elif choices == "exit" or choices == 0: 
        sys.exit(0)
    else:
        print("\n [!] Invalid option. Please choose 0, 1 or 2.")


