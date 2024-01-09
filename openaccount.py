# openaccount.py

import os
import subprocess
from colorama import Fore, Style

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_new_account():
    clear_terminal()
    subprocess.run(['python', os.path.join('manageaccounts', 'createnewaccount.py')])
    clear_terminal()

def update_existing_account():
    clear_terminal()
    subprocess.run(['python', os.path.join('manageaccounts', 'updateexistingaccount.py')])
    clear_terminal()

def open_account_menu():
    print("Options:")
    print("1. Create New Account")
    print("2. Update Existing Account")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        create_new_account()
    elif choice == '2':
        update_existing_account()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    open_account_menu()
