import requests as req
import time 
import shutil
from rich import print

def headers_analysis(url):
   columns ,_ = shutil.get_terminal_size(fallback=(80, 24))
   line,line1 =  "="*columns , "─"*columns
   print(line)
   text = "HTTP HEADER ANALYSIS"
   print(text.center(columns))
   print(line)
   session = req.session()
   start = time.time()
   r = session.get(url)
   end = time.time()
   headers = r.headers
   print(f"[bright_cyan]Target         :[/bright_cyan] {url}")
   print(f"[bright_cyan]Status Code    :[/bright_cyan] {r.status_code}")
   print(f"[bright_cyan]Response Time  :[/bright_cyan] {end - start:.2f} sec")

   print(line1)
   print("[bold bright_white]HTTP Response Headers[/bold bright_white]")
   print(line1)

   for key, value in headers.items():
         print(f"[green]{key:<25}[/green] : {value}")

   print(line) 


