# --- Sources --- #
# Visual Studio Code by Microsoft | IDE used to program code
# Python 3.11.2 by Python Software Foundation | Programming Language used
# Pylance by Microsoft | Language support for Python
# Jupyter by Microsoft | Debugging
# GitHub by GitHub Inc.; Git by Linus Torvalds, Junio C Hamano | Open Source Repository Sync & Version control
# --- 

import os
import json

print()
debug_del = False
if debug_del == True:
    if(os.path.exists("logins.json")):
        os.remove("logins.json")
    if(os.path.exists("config.txt")):
        os.remove("config.txt")


# File Manipulation
def write_to_file(filetype, filename, export): # Avaiable File Formats: txt, json
    if filetype == "json":
        input_json = json.dumps(export, indent=2)
        with open(filename, "w") as l:
            l.write(input_json)
    elif filetype == "txt":
        with open(filename, "w") as l:
            l.write(export)
    else: 
        print("ERROR: file_type not supported.")


# Preferences File creation
if(os.path.exists("config.txt") == False):
    print("ERROR: config.txt failed to load")
    correct_entry = False
    while(correct_entry == False):
        print("Please enter your password requirements\n| Weak (w) | Moderate (m) | Strong (s) |")
        pass_req = input("> ")
        if(pass_req == "w" or pass_req == "m" or pass_req == "s"):
            correct_entry = True
        else:
            print("\nEntry Prompt incorrect! ")
    config_export = (pass_req)
    write_to_file("txt", "config.txt", config_export)
    print("config.txt created...")
pref = open("config.txt", "r") # read pref list 
pass_req = pref.readline()


# Login list Creation
if(os.path.exists("logins.json")): # Check if a login.json file exists
    print("Logins.json Detected...")
else: 
    open("logins.json", "w") # if 'logins.json' doesn't exist, create it and insert dictionary format
    print("ERROR: logins.json not detected")
    format_dict = {"logins": []}
    write_to_file("json", "logins.json", format_dict)
    print("logins.json created... ")

with open("logins.json", "r") as l: # Loads json file and exports it into a readable dictionary for python
    login_dict = json.loads(l.read())
print("logins.json loaded...\nLogins imported successfully!")


# Format For Logins
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


# List Login Function
def list_all():
    print("\n| Logins: ")
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
