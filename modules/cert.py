import requests as req
import shutil
from rich import print
import sys

def cert_analysis(target):
    columns ,_ = shutil.get_terminal_size(fallback=(80, 24))
    _,line1 =  "="*columns , "─"*columns
    web = target[8:]
    print(line1)
    print("[bold yellow][!][/bold yellow] Certificate Transparency lookup is temporarily unavailable.")
    print("[yellow]The external Certificate Transparency service is currently unreachable.[/yellow]")
    print("[yellow]Please try again later.[/yellow]")
    print(line1)