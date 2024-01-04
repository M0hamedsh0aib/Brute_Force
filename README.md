## BruteForce Script
## Discription

BruteForce Python script designed as a Brute-Force Attack Tool, specifically crafted for security testing purposes. This application enables users to assess the robustness of login systems by systematically trying different combinations of usernames and passwords against a target URL. The script supports both GET and POST HTTP methods, offering versatility in evaluating various login systems.

## installation

 Before using PyBruteForce, you need to ensure that the required dependencies are installed. Open a terminal and execute the following command:

bash

pip install requests argparse termcolor

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

## Usage Prerequisites

    Python 3.x
    Required Python packages: requests, argparse, termcolor

## Installation

    Install the required packages using the following command:

    bash

    pip install requests argparse termcolor

    Download the script.

## Command-line Arguments

    -ul or --userwordlist: Path to the usernames wordlist file.
    -pl or --passwordlist: Path to the passwords wordlist file.
    -t or --targeturl: Target URL of the login form.
    -u or --username: Username parameter for the login form.
    -p or --password: Password parameter for the login form.
    -m or --method: HTTP method (get or post) for the login request.
    -e or --error: Optional. Custom error message to detect failed login attempts.

## Python Module Installation
[PyPi Module Link]( https://pypi.org/project/bruteforce-script/1.0/)
```bash
pip install bruteforce-script
```

## Disclaimer
This script is intended for educational and ethical purposes only. Unauthorized use of this script to perform malicious activities is strictly prohibited. The developers are not responsible for any misuse or damage caused by this script.

## Version History
`v1.0`: Bruteforce credentials in websites with error message using GET and POST methods.
