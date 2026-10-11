
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Outil de recherche de points sensibles dans les fichiers .js
#
# J'ai décidé de coder cet outil car, lors d'un pentest,
# il est fastidieux de passer plusieurs minutes à analyser
# manuellement des fichiers JavaScript.
#
# Cet outil permet de gagner du temps.
#!/usr/bin/env python3
#outils de recherche de point sencible dans les chichier .js
# j'ai pensez à coder ce outils cas en vrai pendant un pintest c'est très ennuant de passé des minutes à regarder dans >
#je code ce outils pour allez plus vite.

# pour utiliser ce outils vous devez avoir l'autorisation du deteneur du site web que vous soutaitez attaquer.
# ATTENTION : vous devez disposer de l'autorisation
# du propriétaire du site web avant de réaliser un test.
import time
import requests
import sys
import threading
console = Console()

class Colors:
    RED = "\033[91m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    PURPLE = "\033[95m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    END = "\033[0m"


# Bannière
def banniere():
    print(f"""
{Colors.RED}{Colors.RED}
       888 ,e,                                  d8          
 e88~\888  "  888-~\  d88~\  d88~\  e88~~8e  _d88__  d88~\ 
d888  888 888 888    C888   C888   d888  88b  888   C888   
8888  888 888 888     Y88b   Y88b  8888__888  888    Y88b  
Y888  888 888 888      888D   888D Y888    ,  888     888D 
 "88_/888 888 888    \_88P  \_88P   "88___/   "88_/ \_88P  
  version: 1.0
{Colors.CYAN}👤 Créé par lucifer3d| 📅 {time.strftime('%Y-%m-%d %H:%M:%S')}{Colors.END}
    """)
if __name__ == "__main__":
    banniere()
console.print(
    "[bold red]Extension :[/bold red] [white].js[/white] | "
    "[bold cyan]Threads :[/bold cyan] [white]30[/white] | "
    "[bold yellow]Méthode HTTP :[/bold yellow] [white]GET[/white] | "
    "[bold green]Bonne chance ![/bold green]"
)

# main
