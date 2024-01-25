# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:09:48 2024

@author: Nate P
"""

def main():
    print("Welcome to the URLIPMaker-Util!")

    while True:
        ip = input("\nPlease enter an IP address (*.*.*.* format) or 'quit' to exit: ")

        if ip.lower() == 'quit':
            break

        if check_n_input(ip):
            results = parser(ip)
            print("\nGenerated URLs:")
            for url in results:
                print(url)

            input("\nPress Enter to continue...")
        else:
            print("\nError: Invalid IP format.")
            input("Press Enter to continue...")

def check_n_input(ip):
    # Split the IP address into its components
    parts = ip.split('.')

    # Check if IP has four parts and each part is a valid number between 0 and 255
    if len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
        return True
    else:
        return False

def parser(ip):
    # Replace placeholders with actual IP in URLs
    sources = [
        "https://www.whois.com/whois/*.*.*.*",
        "https://securitytrails.com/list/ip/*.*.*.*",
        "https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a*.*.*.*&run=toolpage",
        "https://www.abuseipdb.com/check/*.*.*.*"
    ]

    return [source.replace("*.*.*.*", ip) for source in sources]

if __name__ == "__main__":
    main()
