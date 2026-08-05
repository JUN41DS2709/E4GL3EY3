import shutil
import sys
import requests as req
from rich import print

def tech_analysis(url):
    columns ,_ = shutil.get_terminal_size(fallback=(80, 24))
    line,line1 =  "="*columns , "─"*columns
    print(line)
    print("[bold bright_white]TECHNOLOGY STACK ANALYSIS[/bold bright_white]")
    print(line)
    session = req.session()
    r = session.get(url)
    if r.status_code == 200:
        print(f"[bold green]Website {url} is reachable.[/bold green]")
        print(line)
        print(f"[bold cyan]Technology Stack Analysis for {url}[/bold cyan]")
        print(line1)
        if server := r.headers.get("Server"):
            print(f"[bold yellow]Server :[/bold yellow] {server}")
        if x_powered_by := r.headers.get("X-Powered-By"):
            print(f"[bold yellow]Language :[/bold yellow] {x_powered_by}")

         # CMS

        if "wordpress" in r.text.lower() or "wp-content" in r.text.lower() or "wp-includes" in r.text.lower() or "wp-json" in r.text.lower():
            print(f"[bold yellow]CMS :[/bold yellow] WordPress")
        if "drupal" in r.text.lower() or "sites/default" in r.text.lower() or "drupal.js" in r.text.lower():
            print(f"[bold yellow]CMS :[/bold yellow] Drupal")
        if "joomla" in r.text.lower() or "com_content" in r.text.lower() or "joomla.js" in r.text.lower():
            print(f"[bold yellow]CMS :[/bold yellow] Joomla")

        # JavaScript Frameworks
        if "react" in r.text.lower() or "react-dom" in r.text.lower():
            print(f"[bold yellow]JavaScript Framework :[/bold yellow] React")
        if "vue" in r.text.lower() or "__VUE__" in r.text.lower():
            print(f"[bold yellow]JavaScript Framework :[/bold yellow] Vue")
        if "angular" in r.text.lower() or "ng-app" in r.text.lower() or "ng-version" in r.text.lower():
            print(f"[bold yellow]JavaScript Framework :[/bold yellow] Angular")
        if "_next/" in r.text.lower() or "__NEXT_DATA__" in r.text.lower():
             print(f"[bold yellow]JavaScript Framework :[/bold yellow] NEXT JS")
        if "nuxt" in r.text.lower() or "__NUXT__" in r.text.lower():
             print(f"[bold yellow]JavaScript Framework :[/bold yellow] Nuxt JS")

        # JS libraries
        if "jquery" in r.text.lower() or "jquery.min.js" in r.text.lower():
            print(f"[bold yellow]JavaScript Library :[/bold yellow] jQuery")    
        if "lodash" in r.text.lower() or "lodash.min.js" in r.text.lower():
            print(f"[bold yellow]JavaScript Library :[/bold yellow] Lodash")
        if "moment" in r.text.lower() or "moment.min.js" in r.text.lower():
            print(f"[bold yellow]JavaScript Library :[/bold yellow] Moment.js")
        if "axios" in r.text.lower() or "axios.min.js" in r.text.lower():
            print(f"[bold yellow]JavaScript Library :[/bold yellow] Axios")


        # CSS Frameworks
        if "bootstrap" in r.text.lower() or "bootstrap.min.css" in r.text.lower():
            print(f"[bold yellow]CSS Framework :[/bold yellow] Bootstrap")
        if "tailwind" in r.text.lower() or "tailwind.min.css" in r.text.lower():
            print(f"[bold yellow]CSS Framework :[/bold yellow] Tailwind CSS")
        if "bulma" in r.text.lower() or "bulma.min.css" in r.text.lower():
            print(f"[bold yellow]CSS Framework :[/bold yellow] Bulma")
        if "foundation" in r.text.lower() or "foundation.min.css" in r.text.lower():
            print(f"[bold yellow]CSS Framework :[/bold yellow] Foundation")
        if "materialize" in r.text.lower() or "materialize.min.css" in r.text.lower():
            print(f"[bold yellow]CSS Framework :[/bold yellow] Materialize")

        # CDN
        if "cloudflare" in r.text.lower() or "cdn-cgi" in r.text.lower():
            print(f"[bold yellow]CDN :[/bold yellow] Cloudflare")
        if "akamai" in r.text.lower() or "akamaihd" in r.text.lower():
            print(f"[bold yellow]CDN :[/bold yellow] Akamai")
        if "aws" in r.text.lower() or "amazonaws" in r.text.lower():
            print(f"[bold yellow]CDN :[/bold yellow] Amazon CloudFront")
        if "fastly" in r.text.lower() or "fastly.net" in r.text.lower():
            print(f"[bold yellow]CDN :[/bold yellow] Fastly")
        if  "maxcdn" in r.text.lower() or "bootstrapcdn" in r.text.lower():
            print(f"[bold yellow]CDN :[/bold yellow] MaxCDN")
        session.close()
        