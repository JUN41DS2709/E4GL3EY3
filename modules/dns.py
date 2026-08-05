import dns.resolver
from rich import print
import shutil

def dns_anlysis(web):
    url = web[8:]
    columns ,_ = shutil.get_terminal_size(fallback=(80, 24))
    line,line1 =  "="*columns , "─"*columns
    print(line)
    print("\nDNS RECORD ANALYSIS\n")
    print(line)

    print(f"\nTarget Domain : {url}\n")

    print(line1)
    print("\nA Records (IPv4)\n")
    print(line1)
    # 1. Get IPv4 Addresses (A Records)
    try:
        a_record = dns.resolver.resolve(url , 'A')
        for ip in a_record:
            print(f"[cyan1] IPv4 Address: {ip.to_text()} [/cyan1]")
    except Exception as e:
        print(f"[bright_red] Error fetching A record: {e} [/bright_red]")
    # 2.  Get IPv6 Addresses (AAAA Records)

    print(line1)
    print("\nAAAA Records (IPv6)\n")
    print(line1)

    try:
            a_record = dns.resolver.resolve(url , 'AAAA')
            for ip in a_record:
                print(f"[cyan1] IPv6 Address: {ip.to_text()} [/cyan1]")
    except Exception as e:
            print(f"[bright_red] Error fetching A record: {e} [/bright_red]")

    print(line1)
    print("\nMX Records\n")
    print(line1)
    
    # 3. Get Mail Servers (MX Records)    
    try:
        mx_record = dns.resolver.resolve(url , 'MX')
        for server in mx_record:
            print(f"[cyan1] Mail Server: {server.exchange} (Preference: {server.preference}) [/cyan1]")
    except Exception as e:
            print(f"[bright_red] Error fetching MX record: {e} [/bright_red]")

    print(line1)
    print("\nCNAME Records\n")
    print(line1)
    
    # 4. Get CNAME Servers (CNAME Records)
    try:
    # Query the CNAME record for a subdomain
        answers = dns.resolver.resolve(url, 'CNAME')
    
        for rdata in answers:
        # Use .target to print the canonical domain name
            print(f"[cyan1] CNAME : {rdata.target} [/cyan1]")
        
    except dns.resolver.NoAnswer:
        print("[bright_red] The domain exists, but has no CNAME record.[/bright_red]")
    except dns.resolver.NXDOMAIN:
        print("[bright_red] The domain name does not exist.[/bright_red]")
    except Exception as e:
         print(f"[bright_red] An error occurred: {e} [/bright_red]")

    print(line1)
    print("\nTXT Records\n")
    print(line1)

    # 5. Get TXT records (TXT Records)
    try:
    # Query the TXT  record for a subdomain
        answers = dns.resolver.resolve(url, 'TXT')
        for rdata in answers:
    # TXT records can contain multiple string segments
            for string in rdata.strings:
    # Decode the binary data to a normal string
                print(f"[cyan1] TXT Record: {string.decode('utf-8')} [/cyan1]")
        
    except dns.resolver.NoAnswer:
        print("[bright_red] The domain exists, but has no TXT record.[/bright_red] ")
    except dns.resolver.NXDOMAIN:
        print("[bright_red] The domain name does not exist.[/bright_red]")
    except Exception as e:
        print(f"[bright_red] An error occurred: {e} [/bright_red]")

    
    print(line1)
    print("\nNS Records\n")
    print(line1)

    # 6. Get NS server (Name server)
    try:
    # Query NS records for a domain
        ns_answers = dns.resolver.resolve(url, 'NS')
    
        for rdata in ns_answers:
        # Use .target to get the nameserver domain name
            print(f"[cyan1] Name Server: {rdata.target} [/cyan1]")
        
    except dns.resolver.NoAnswer:
        print("[bright_red] No NS records found.[/bright_red]")
    except dns.resolver.NXDOMAIN:
         print("[bright_red] The domain does not exist. [/bright_red]")