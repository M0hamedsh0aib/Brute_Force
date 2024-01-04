## BruteForce Script
## Discription

BruteForce Python script designed as a Brute-Force Attack Tool, specifically crafted for security testing purposes. This application enables users to assess the robustness of login systems by systematically trying different combinations of usernames and passwords against a target URL. The script supports both GET and POST HTTP methods, offering versatility in evaluating various login systems.

## Prerequesties

Python 3.x

Required Libraries

Wordlist files

## Installation

 Before using PyBruteForce, you need to ensure that the required dependencies are installed. Open a terminal and execute the following command:

```bash
pip install requests argparse termcolor
```

This command installs the necessary Python libraries: requests for HTTP requests, argparse for handling command-line arguments, and termcolor for enhancing console output.

PyPi Module Link

 [PyPi Module Link]( https://pypi.org/project/bruteforce-script/1.0/)
```bash
pip install bruteforce-script
```
                                                                                                         
## Features

    HTTP Methods: Supports both GET and POST methods for login attempts.
   
    Wordlist Input: Utilizes wordlists for usernames and passwords for comprehensive bruteforcing.
   
    Error Handling: Customizable error message handling to identify failed login attempts.
   
    Visual Interface: Provides a visually appealing banner for user interaction.

## Run Command
```
python script.py -ul <user_wordlist> -pl <password_wordlist> -t <target_url> -u <username> -p <password> -m <method> -e <error_message>
```

## Screeenshots
 ![WhatsApp Image 2024-01-04 at 11 34 37_4dfce529](https://github.com/M0hamedsh0aib/Brute_Force/assets/108838188/cf5c796e-2364-45b9-b7bb-6c9bef2e2a28)
 ![WhatsApp Image 2024-01-04 at 11 34 37_c0f22c20](https://github.com/M0hamedsh0aib/Brute_Force/assets/108838188/24ec9a53-0e1d-4248-a018-2e7693c5271d)

## Disclaimer
This script is intended for educational and ethical purposes only. Unauthorized use of this script to perform malicious activities is strictly prohibited. The developers are not responsible for any misuse or damage caused by this script.
 

 
