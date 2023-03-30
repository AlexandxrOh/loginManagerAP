# Login Manager by Alexander Oh 
# MIT License

# --- Sources --- #
# Visual Studio Code by Microsoft | IDE used to program code
# Python 3.11.2 by Python Software Foundation | Programming Language used
# Pylance by Microsoft | Language support for Python
# Jupyter by Microsoft | Debugging
# GitHub by GitHub Inc.; Git by Linus Torvalds, Junio C Hamano | Open Source Repository Sync & Version control
# --- 

import os
import json

letter_list, upper_letter_list = [list("abcdefghijklmnopqrstuvwxyz")], [list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
number_list = [list("0123456789")]
symbol_list = [list("!?,./\|@#$%^&*()-_=+:;")]

class login_entry: 
    def __init__(self, login, username, password): 
        self.login = login
        self.username = username
        self.password = password
    
    def __str__(self): # String Return if login_entry is called, mostly used for debugging
        return f"Login: {self.login}, Username: {self.username}, Password: {self.password}"
    
# set debug_json to 'True' to enter a example login into the 'logins.json' file; CAUTION: WILL OVERRIDE 'logins.lson' FILE
debug_json = True
if(debug_json == True):
    print("Debug Entry Appended to 'logins.json'...")
    debug_dict = {
        "logins": [
            {
                "login": "testLogin",
                "username": "testUsername",
                "password": "testPassword"
            }
        ]
    }
    debug_dict_json = json.dumps(debug_dict, indent=2)
    with open("logins.json", "w") as l:
        l.write(debug_dict_json)

if(os.path.exists("logins.json")): # Check if a login.json file exists
    print("Login json Detected...")
    with open("logins.json", "r") as l: # Loads json file and exports it into a readable dictionary for python
        login_dict = json.loads(l.read())
else: 
    open("logins.json", "w")

print("\nCommand Line Login Manager\nAuthor: Alexander Oh | License: MIT Open Source\n| New Login (n) | Login List (l) |")
prompt = input(">")
if(prompt == "n"):
    print("\nNew Login Entry")
    new_login = input("| Login Name: ") 
    new_user = input("| Username: ")
    # Password will go here