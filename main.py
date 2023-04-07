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
debug_del = True
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
        print("Please enter your password requirements\n| Weak (w) | Moderate (m) | Strong (s) | None (n) |")
        pass_req = input("> ")
        if(pass_req == "w" or pass_req == "m" or pass_req == "s" or pass_req == "n"):
            correct_entry = True
        else:
            print("\nEntry Prompt incorrect! ")
    config_export = (pass_req)
    write_to_file("txt", "config.txt", config_export)
    print("config.txt created...")
pref = open("config.txt", "r") # read pref list 
pass_req = pref.readline()


# Login list Creationasd
if(os.path.exists("logins.json")): # Check if a login.json file existsasd
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


# Password Generation 
def character_filter(list_type, char): # Basic layout edited from "filter() in python" article @ geeksforgeeks.org
    lowercase_list = list("abcdefghijklmnopqrstuvwxyz")
    uppercase_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    number_list = list("1234567890")
    symbol_list = list("?!<>,./@#$%^&*()_+-=[]}{:;")
    if (list_type == "lowercase"): # Ignore this else if vomit
        if (char in lowercase_list):
            return True
        else: 
            return False
    elif (list_type == "uppercase"):
        if (char in uppercase_list):
            return True
        else: 
            return False
    elif (list_type == "number"):
        if (char in number_list):
            return True
        else:
            return False 
    elif (list_type == "symbol"):
        if (char in symbol_list):
            return True
        else: 
            return False
    else:
        print("ERROR: Character filter list_type not compatible! ")

def pass_check(password):
    password_list = list(password)
    pass_strength_check = False
    if(pass_req == "w"):
        upper_req, lower_req, sym_req, num_req, len_req = 1, 1, 0, 0, 6
    elif(pass_req == "m"):
        upper_req, lower_req, sym_req, num_req, len_req = 1, 1, 1, 1, 16
    elif(pass_req == "s"):
        upper_req, lower_req, sym_req, num_req, len_req = 3, 3, 2, 3, 16
    elif(pass_req == "n"):
        pass_strength_check = True

    filtered_upper, filtered_lower, filtered_sym, filtered_num = [], [], [], []
    for character in password_list:
        if(character_filter("lowercase", character)):
            filtered_lower.append(character)
            continue
        elif(character_filter("uppercase", character)):
            filtered_upper.append(character)
            continue
        elif(character_filter("symbol", character)):
            filtered_sym.append(character)
            continue
        elif(character_filter("number", character)):
            filtered_num.append(character)
            continue
    
    if(pass_strength_check == False):
        print("\nUpper: " + str(len(filtered_upper)) + "/" + str(upper_req))
        print("Lowercase: " + str(len(filtered_lower)) + "/" + str(lower_req))
        print("Numbers: " + str(len(filtered_num)) + "/" + str(num_req))
        print("Symbols:  " + str(len(filtered_sym)) + "/" + str(sym_req))
        print("Total Length: " + str(len(password_list)) + "/" + str(len_req))
        filtered_upper, filtered_lower, filtered_sym, filtered_num, password_list = len(filtered_upper), len(filtered_lower), len(filtered_sym), len(filtered_num), len(password)
        if(filtered_upper >= upper_req and filtered_lower >= lower_req and filtered_sym >= filtered_sym and filtered_num >= num_req and password_list >= len_req):
            print("\n Password Accepted")
            return "Password Accepted"
        else:
            print("\n Password Not Accepted, please enter a new password.")
            return "Password Not Accepted"

    elif(pass_strength_check == True):
        filtered_upper, filtered_lower, filtered_sym, filtered_num, password_list = len(filtered_upper), len(filtered_lower), len(filtered_sym), len(filtered_num), len(password)
        if(filtered_lower >= 3 and filtered_upper >= 3 and filtered_num >= 3 and filtered_sym >= 2 and password_list >= 16):
            pass_strength = "Strong"
        elif(filtered_lower >= 1 and filtered_upper >= 1 and filtered_num >= 1 and filtered_sym >= 1 and password_list >= 16):
            pass_strength = "Moderate"
        else:
            pass_strength = "Weak"
        print("Password Strength: " + pass_strength)
        return pass_strength
            
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

print()