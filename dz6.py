# Cheak Readme.md file

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(Fore.RED + 'Цей текст буде червоним' + Style.RESET_ALL)
print(Back.GREEN + 'Цей текст буде на зеленому фоні' + Style.RESET_ALL)
print(Style.BRIGHT + 'Цей текст буде яскравим' + Style.RESET_ALL)
print(Style.BRIGHT + Fore.RED + Back.GREEN + 'Все разом' + Style.RESET_ALL)

print("")

print("Всі кольори!\n")

print(Fore.BLACK + 'BLACK')
print(Fore.BLUE + 'BLUE')
print(Fore.CYAN + 'CYAN')
print(Fore.GREEN + 'GREEN')
print(Fore.LIGHTBLACK_EX + 'LIGHTBLACK_EX')
print(Fore.LIGHTBLUE_EX + 'LIGHTBLUE_EX')
print(Fore.LIGHTCYAN_EX + 'LIGHTCYAN_EX')
print(Fore.LIGHTGREEN_EX + 'LIGHTGREEN_EX')
print(Fore.LIGHTMAGENTA_EX + 'LIGHTMAGENTA_EX')
print(Fore.LIGHTRED_EX + 'LIGHTRED_EX')
print(Fore.LIGHTWHITE_EX + 'LIGHTWHITE_EX')
print(Fore.LIGHTYELLOW_EX + 'LIGHTYELLOW_EX')
print(Fore.MAGENTA + 'MAGENTA')
print(Fore.RED + 'RED')
print(Fore.RESET + 'RESET')
print(Fore.WHITE + 'WHITE')
print(Fore.YELLOW + 'YELLOW')

colorama.deinit()
