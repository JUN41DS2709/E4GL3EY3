import whois
from rich import print
import shutil

def whois_analysis(target):
    url = target[8:]
    columns ,_ = shutil.get_terminal_size(fallback=(80, 24))
    line,_ =  "="*columns , "─"*columns
    try:
        print(f"\n[bold green]Performing WHOIS analysis for {url}...[/bold green]")
        w = whois.whois(url)
        print("\n[bold green]WHOIS Information:[/bold green]")
        print(line)
        print(f"[bold cyan]Domain Name:[/bold cyan] {w.domain_name}")
        print(f"[bold cyan]Registrar:[/bold cyan] {w.registrar}")
        print(f"[bold cyan]Creation Date:[/bold cyan] {w.creation_date}")
        print(f"[bold cyan]Expiration Date:[/bold cyan] {w.expiration_date}")
        print(f"[bold cyan]Name Servers:[/bold cyan] {w.name_servers}")
        print(f"[bold cyan]Status:[/bold cyan] {w.status}")
        print(f"[bold cyan]Emails:[/bold cyan] {w.emails}")
        print(f"[bold cyan]DNSSEC:[/bold cyan] {w.dnssec}")
        print(f"[bold cyan]Registrar WHOIS Server:[/bold cyan] {w.registrar_whois_server}")
        print(f"[bold cyan]Registrar URL:[/bold cyan] {w.registrar_url}")
        print(f"[bold cyan]Updated Date:[/bold cyan] {w.updated_date}")
        print(f"[bold cyan]Name:[/bold cyan] {w.name}")
        print(f"[bold cyan]Org:[/bold cyan] {w.org}")
        print(f"[bold cyan]Address:[/bold cyan] {w.address}")
        print(f"[bold cyan]City:[/bold cyan] {w.city}")
        print(f"[bold cyan]State:[/bold cyan] {w.state}")
        print(f"[bold cyan]Zipcode:[/bold cyan] {w.zipcode}")
        print(f"[bold cyan]Country:[/bold cyan] {w.country}")
        print(line)

    except Exception as e:
        print(f"[bold red]Error performing WHOIS analysis: {e}[/bold red]")
        print(f"[bold red]Please check your internet connection or the domain name and try again.[/bold red]")