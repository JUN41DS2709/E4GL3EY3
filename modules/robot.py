import requests as req
import shutil
from rich import print 
import sys

def robot_analysis(target):
    columns ,_ = shutil.get_terminal_size(fallback=(80, 24))
    line,line1 =  "="*columns , "─"*columns
    web = target
    session = req.session()
    r = session.get(web+"/robots.txt")
    print(f"Status code : {r.status_code}")
    if r.status_code == 200:
        print(line)
        print(f"[bold green]Robots.txt file found for {web}[/bold green]")
        print(line)
        print(f"[bold cyan]Robots.txt Content :[/bold cyan]")
        print(line1)
        print(r.text)
        print(line1)
    else:
        print(f"[bold red]Robots.txt file not found for {web} or doesn't exist[/bold red]")

    choice = input("Export robots.txt? (y/n) : $ > ")
    if choice.lower() == "y":
        with open("robots.txt", "w") as f:
            f.write(r.text)
    elif choice.lower() == "n":
        sys.exit(0)

    session.close()
