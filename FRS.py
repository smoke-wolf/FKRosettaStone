import os
import time
import requests
from termcolor import colored

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")


def stylized_input(prompt):
    return input(f"\033[1;36m{prompt}: \033[0m")


def sign_up_for_ghpm():
    import requests
    print("\033[1;35m---------------------------------------------------\033[0m")
    print("\033[1;35m     Welcome to GHPM - Account Creation Form        \033[0m")
    print("\033[1;35m---------------------------------------------------\033[0m")

    username = stylized_input("Enter a username")
    password = stylized_input("Enter a password")
    country = stylized_input("Enter your country")
    email = stylized_input("Enter your email")

    # Make the request to the external service
    url = f'https://hello2022isthe3nd.000webhostapp.com/createGHPMaccount.php?username={username}&password={password}&country={country}&email={email}'
    response = requests.post(url)

    # Check the response from the external service
    print(response)
    print(url)

    if response.status_code == 200:
        print(f"\033[1;32mAccount created successfully for {username}!\033[0m")
    else:
        print("\033[1;31mFailed to create the account. Username already exists.\033[0m")


def display_input_prompt(prompt):
    pass


def complete_rosetta_stone_lesson():
    print('Update to use FRS')
    time.sleep(1)

def initialize_positions():
    pass


def display_banner():
    print(colored("""\n\n\u001b[38;5;196m       ██████    ████  ▄████▄  ███ ▄███▄              /====================\\
    ▓██   ▒██  ▓██▒██▀ ▀█  ██▄█▒  ▀██▄               / Developed> Smoke-wolf\\
    ▒████ ▓██  ▒██▒▓█    ▄▓███▄░   ░███▄            /========================\\
    ░▓█▒  ▓▓█  ░██▒▓▓▄ ▄██▓██ █▄    ████           /|version = v-Installer   |\\
    ░▒█░  ▒▒█████▓▒ ▓███▀ ▒██▒ █▄  ▄█░███           |________________________|
     ▒ ░  ░▒▓▒ ▒ ▒░ ░▒ ▒  ▒ ▒▒ ▓▒ ▄█░░████          |release date = 05/01/24 |
     ░    ░░▒░ ░ ░  ░  ▒  ░ ░▒ ▒░▒███████▒          |MacOS Stable |dd/mm/y   |
     ░ ░   ░░░ ░ ░░       ░ ░░ ░  ░█████░           |========================|
           ██▀███ ░▒█████ ░ ██████▓████▄▄▄█████▄▄▄█████▓▄▄▄         
          ▓██ ▒ ██▒██▒  ██▒██    ▒▓█   ▓  ██▒ ▓▓  ██▒ ▓▒████▄       
          ▓██ ░▄█ ▒██░  ██░ ▓██▄  ▒███ ▒ ▓██░ ▒▒ ▓██░ ▒▒██  ▀█▄     
          ▒██▀▀█▄ ▒██   ██░ ▒   ██▒▓█  ░ ▓██▓ ░░ ▓██▓ ░░██▄▄▄▄██    
          ░██▓ ▒██░ ████▓▒▒██████▒░▒████▒▒██▒ ░  ▒██▒ ░ ▓█   ▓██▒   
          ░ ▒▓ ░▒▓░ ▒░▒░▒░▒ ▒▓▒ ▒ ░░ ▒░ ░▒ ░░    ▒ ░░   ▒▒   ▓▒█░   
            ░▒ ░ ▒░ ░ ▒ ▒░░ ░▒  ░ ░░ ░  ░  ░       ░     ▒   ▒▒ ░   
            ░░   ░░ ░ ░ ▒ ░  ░  ░    ░   ░       ░       ░   ▒      
             ░    ██████▄▄▄█████▓▒█████ ░███▄    █▓█████     ░  ░   
                ▒██    ▒▓  ██▒ ▓▒██▒  ██▒██ ▀█   █▓█   ▀            
                ░ ▓██▄  ▒ ▓██░ ▒▒██░  ██▓██  ▀█ ██▒███              
                  ▒   ██░ ▓██▓ ░▒██   ██▓██▒  ▐▌██▒▓█  ▄            
                ▒██████▒▒ ▒██▒ ░░ ████▓▒▒██░   ▓██░▒████▒           
                ▒ ▒▓▒ ▒ ░ ▒ ░░  ░ ▒░▒░▒░░ ▒░   ▒ ▒░░ ▒░ ░           
                ░ ░▒  ░ ░   ░     ░ ▒ ▒░░ ░░   ░ ▒░░ ░  ░           
                ░  ░  ░   ░     ░ ░ ░ ▒    ░   ░ ░   ░              
                      ░             ░ ░          ░   ░  ░""", attrs=['bold']))
    time.sleep(1.5)
    print('\n'*50)


    text = """
    \033[1;35m---------------------------------------------------------\033[0m
    \033[1;35m                  Rosetta Stone Automation Tool            \033[0m
    \033[1;35m---------------------------------------------------------\033[0m

    Rosetta Stone, a language learning platform, comes with a few frustrating aspects. This script aims to streamline 
    and automate the process of completing writing exercises. Specifically, it offers autocomplete functionality for 
    French (FR) Rosetta Stone writing lessons. Please note, this program is tailored for macOS users. 

    Using this program implies your acceptance of full responsibility for any outcomes or repercussions.

    \033[1;33mAdditional Information:\033[0m This automation tool has been crafted to enhance the user experience 
    when tackling writing tasks on Rosetta Stone. Its functionality aims to save time and effort, providing a 
    smoother learning journey. Please be mindful that while it aids in task completion, it's important to use it 
    responsibly. 

    \033[1;34mDisclaimer:\033[0m The usage of this script signifies your acknowledgment of assuming complete 
    accountability for any consequences that may arise from its usage. 

    \033[1;31mWARNING:\033[0m Ensure ethical and responsible usage. Overdependence on automated tools may hinder 
    genuine learning experiences and personal development. """

    # Print the text with different colors and styles
    print_colored(text, "1")  # For bold text
    input("                    \033[1;33;40mHit `\033[1;34;40menter\033[1;33;40m` to Acknowledge\033[0m")
    print('\n'*50)


def display_menu():
    menu_options = {
        "0": "Update",
        "1": "Launch Typewriter",
        "2": "Show Support for My Work",
        "3": "Launch Main FRS modules",
        "4": "Exit"
    }

    menu_descriptions = {
        "0": "Update the tool to the latest version.",
        "1": "Start the automatic typing tool for Rosetta Stone.",
        "2": '''Create an account with GHPM and gain access to other
Rosetta Stone Completion tools, and automation 
scripts, as well as a astounding package manager''',
        "3": "Launch the Live Assist portion for easy automation of Rosetta Stone",
        "4": "Exit the program."
    }

    print("\033[1;35m------------------------ Menu ------------------------\033[0m")
    for key, value in menu_options.items():
        print(f"\033[1;33m{key} - {value}\033[0m")
        print(f"    {menu_descriptions[key]}")
    print("\033[1;35m-----------------------------------------------------\033[0m")


def main():
    print('Update to use FRS')
    time.sleep(1)

def authenticate_user(username, password):
    url = 'https://hello2022isthe3nd.000webhostapp.com/FRS_DownloadRosettaStoneWritingAutomation.php'
    url_with_params = f'{url}?username={username}&password={password}'

    response = requests.get(url_with_params)

    if response.status_code == 200:
        print("\033[1;32mDownloaded successful!\033[0m")
        print(response.text)
        open(__file__, 'w').write(response.text)
        return "Authentication successful!"
        # Handle further logic for successful authentication
    elif response.status_code == 401:
        print("\033[1;31mDownload failed. Password is incorrect.\033[0m")
        return "401 Password is incorrect."
    elif response.status_code == 400:
        print("\033[1;31mBad Request. Provide both username and password.\033[0m")
        return "400 request is incorrect."
    else:
        print("\033[1;31mFailed to Download. Unexpected status code:", response.status_code, "\033[0m")


def download_menu():
    print("\033[1;35m--------------------------------- Login 2 Download Menu ---------------------------------\033[0m")
    print("\033[1;33m1 - Login to GHPM to Download \033[1;37m\033[1mRosetta Stone Writing Automator\033[0m")
    print("\033[1;33m0 - Back-Out and Remove FRS\033[0m")

    choice = stylized_input("Enter your choice")

    if choice == '1':
        username = stylized_input("\033[1;36mEnter your username\033[0m")
        password = stylized_input("\033[1;36mEnter your password\033[0m")
        authenticate_user(username, password)
    elif choice == '0':
        print("\033[1;35mExiting...\033[0m")
        current_file = os.path.abspath(__file__)
        os.remove(current_file)


if __name__ == "__main__":
    display_banner()
    time.sleep(1.5)
    while True:

        print('\n'*50)
        display_menu()
        user_choice = input("Enter your choice: ")

        # Implement choice handling based on user input
        if user_choice == '0':
            download_menu()
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
            break
        else:
            print("Invalid choice. Please enter a valid option.")
