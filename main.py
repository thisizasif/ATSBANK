import os
import subprocess
import sys
from colorama import Fore, Style

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def open_account():
    clear_terminal()
    subprocess.run(['python', 'openaccount.py'])
    clear_terminal()

def print_menu():
    clear_terminal()
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print("  ╔════════════════════════════════════╗")
    print("  ║           My Awesome App           ║")
    print("  ╚════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Options:{Style.RESET_ALL}")
    print(f"1. {Fore.BLUE}Open Account{Style.RESET_ALL}")
    print(f"2. {Fore.RED}Quit{Style.RESET_ALL}")

def main():
    while True:
        print_menu()

        choice = input(f"{Fore.YELLOW}Enter your choice (1 or 2): {Style.RESET_ALL}")

        if choice == '1':
            open_account()
        elif choice == '2':
            clear_terminal()
            print(f"{Fore.YELLOW}Thank you for using My Awesome App! Goodbye!{Style.RESET_ALL}")
            sys.exit()
        else:
            print(f"{Fore.RED}Invalid choice. Please enter 1 or 2.{Style.RESET_ALL}")
            input(f"{Fore.MAGENTA}Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
