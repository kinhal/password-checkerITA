import re
from colorama import Fore, Style

def check_password_strength(password):
    length = len(password)
    if length < 8:
        return Fore.RED + "Debole: la password deve avere almeno 8 caratteri." + Style.RESET_ALL

    score = 0

    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 4 and length >= 12:
        return Fore.GREEN + "Molto forte" + Style.RESET_ALL
    elif score >= 3:
        return Fore.MAGENTA + "Forte" + Style.RESET_ALL
    elif score == 2:
        return Fore.YELLOW + "Media" + Style.RESET_ALL
    else:
        return Fore.RED + "Debole" + Style.RESET_ALL

def main():
    pwd = input(Fore.GREEN + "Inserisci la password da verificare: " + Style.RESET_ALL)
    result = check_password_strength(pwd)
    print(Fore.GREEN + f"Valutazione: {result}" + Style.RESET_ALL)
    input(Fore.GREEN + "\nPremi un tasto per uscire..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
