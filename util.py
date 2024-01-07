import requests


def clear(lines):
    print('\n'*lines)

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def getURL(username, password, country, email):
    return f'https://hello2022isthe3nd.000webhostapp.com/createGHPMaccount.php?username={username}&password={password}&country={country}&email={email}'

def stylized_input(prompt):
    return input(f"\033[1;36m{prompt}: \033[0m")

def authenticate_user(username, password):
    url = 'https://hello2022isthe3nd.000webhostapp.com/FRS_DownloadRosettaStoneWritingAutomation.php'
    url_with_params = f'{url}?username={username}&password={password}'

    response = requests.get(url_with_params)

    if response.status_code == 200:
        print("\033[1;32mDownloaded successful!\033[0m")
        print(response.text)
        open("core.py", 'w').write(response.text)
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

def sign_up_for_ghpm():
    print("\033[1;35m---------------------------------------------------\033[0m")
    print("\033[1;35m     Welcome to GHPM - Account Creation Form        \033[0m")
    print("\033[1;35m---------------------------------------------------\033[0m")

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
