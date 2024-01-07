import os
import sys

import time

import requests

from termcolor import colored
import getpass

from util import *
from core import *
from text import *


class FRS:
    def __init__(self):
        self.bannertext = bannerText
        self.disclaimerText = disclaimerText
        self.runFlag = True

    def display_banner(self):
        print(colored(bannerText, attrs=['bold']))
        time.sleep(1.5)
        clear(50)

        # Print the text with different colors and styles
        print_colored(disclaimerText, "1")  # For bold text
        input()
        clear(50)

    def user_input_and_validation(self):
        user_choice = input("Enter choice: ")

        if user_choice == '0':
            self.download_menu()
            time.sleep(1)

        elif user_choice == '1':
            complete_rosetta_stone_lesson()
            time.sleep(1)

        elif user_choice == '2':
            sign_up_for_ghpm()
            time.sleep(1)

        elif user_choice == '3':
            main()
            time.sleep(1)

        elif user_choice == '4':
            print("Exiting...")
            self.runFlag = False
            
        else:
            print("Invalid choice. Please enter a valid option.")

    def download_menu(self):
        print(downloadMenuText)

        choice = stylized_input("Enter your choice")

        if choice == '1':
            username = stylized_input("\033[1;36mEnter your username\033[0m")
            password = getpass.getpass("\033[1;36mEnter your password\033[0m: ")
            authenticate_user(username, password)

        elif choice == '0':
            print("\033[1;35mExiting...\033[0m")
            current_file = os.path.abspath(__file__)
            os.remove(current_file)
    
    def sign_up_for_ghpm(self):
        print("""\033[1;35m---------------------------------------------------\033
\033[1;35m     Welcome to GHPM - Account Creation Form        \033[0m
\033[1;35m---------------------------------------------------\033[0m""")

        username = stylized_input("Enter a username")
        password = stylized_input("Enter a password")
        country = stylized_input("Enter your country")
        email = stylized_input("Enter your email")

        # Make the request to the external service
        url = getURL(username, password, country, email)
        response = requests.post(url)

        # Check the response from the external service
        print(response)
        print(url)

        if response.status_code == 200:
            print(f"\033[1;32mAccount created successfully for {username}!\033[0m")
        else:
            print("\033[1;31mFailed to create the account. Username already exists.\033[0m")

    def run(self):
        self.display_banner()

        while self.runFlag:
        
            clear(50)
            print(menuText)
            self.user_input_and_validation()
        
        sys.exit()


if __name__ == "__main__": #==============================================================
    cli = FRS()
    cli.run()
