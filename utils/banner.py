import pyfiglet
from rich.console import Console

console = Console(highlight=False)

def show_banner():
    f = pyfiglet.figlet_format(
        "E4GL3EY3",
        font="doom",
        justify="center",
        width=80
    )

    console.print(f"[red3]{f.rstrip()}[/red3]")

    text = "'The Eagle Sees What Others Overlook.'"
    console.print(f"[yellow]{text.center(80)}[/yellow]")

    console.print("[green]$ Passive Reconnaissance Framework[/green]")
    console.print("[green]$ Version : 0.1.0[/green]")
    console.print("[green]$ Author  : JUN41D[/green]")