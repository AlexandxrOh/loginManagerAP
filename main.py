# --- Sources --- #
# Visual Studio Code by Microsoft | IDE used to program code
# Python 3.11.2 by Python Software Foundation | Programming Language used
# Pylance by Microsoft | Language support for Python
# Jupyter by Microsoft | Debugging
# GitHub by GitHub Inc.; Git by Linus Torvalds, Junio C Hamano | Open Source Repository Sync & Version control
# --- 

# make preferences functionality


import os
import json

name = ""

# Preferences File creation
if(os.path.exists("config.txt") == False):
    print("ERROR: config.txt failed to load")
    open("config.txt", "w")
    print("config.txt created...")

if(os.path.exists("logins.json")): # Check if a login.json file exists
    print("Logins.json Detected...")
else: 
    open("logins.json", "w") # if 'lgons.json' doesn't exist, create it and insert dictionary format
    print("ERROR: logins.json not detected")
    format_dict = {"logins": []}
    format_dict_json = json.dumps(format_dict, indent=2)
    with open("logins.json", "r+") as l:
        l.write(format_dict_json)
    print("logins.json created... ")

with open("logins.json", "r") as l: # Loads json file and exports it into a readable dictionary for python
    login_dict = json.loads(l.read())
print("logins.json loaded...\nLogins imported successfully!")

class login_entry: 
    def __init__(self, login, username, password): 
        self.login = login
        self.username = username
        self.password = password
    
    def __str__(self): # String Return if login_entry is called, mostly used for debugging
        return f"Login: {self.login}, Username: {self.username}, Password: {self.password}"
    
    def add_login(self):
        new_login = {
            "login": self.login,
            "username": self.username,
            "password": self.password
        }
        login_dict["logins"].append(new_login)

def write_to_json(entry):
    login_dict_json = json.dumps(login_dict, indent=2)
    with open("logins.json", "w") as l:
        l.write(login_dict_json)

def list_all():
    print("\n| " + name + "'s Logins")
    for x in range(len(login_dict["logins"])):
        print("\nLogin " + str(x + 1) + ":")
        print(login_dict["logins"][x]["login"])
        print(login_dict["logins"][x]["username"])
        print(login_dict["logins"][x]["password"])


# set debug_json to 'True' to enter a example login into the 'logins.json' file; CAUTION: WILL OVERRIDE 'logins.lson' FILE
debug_json = True
if(debug_json):
    print("DEBUG: Entry Appended to 'logins.json'...")
    debug_dict = {
        "logins": [
            {
                "login": "testLogin",
                "username": "testUsername",
                "password": "testPassword"
            },
            {
                "login": "testLogin2",
                "username": "testUsername2",
                "password": "testPassword2"
            }
        ]
    }
    debug_dict_json = json.dumps(debug_dict, indent=2)
    with open("logins.json", "w") as l:
        l.write(debug_dict_json)
