# Login Manager by Alexander Oh 
# MIT License

# --- Sources --- #
# Visual Studio Code by Microsoft | IDE used to program code
# Python 3.11.2 by Python Software Foundation | Programming Language used
# Pylance by Microsoft | Language support for Python
# Jupyter by Microsoft | Debugging
# GitHub by GitHub Inc.; Git by Linus Torvalds, Junio C Hamano | Open Source Repository Sync & Version control
# --- 

usernameList = [] # Holds all saved logins
passwordList = []
loginNameList = []

def homeScreen():
    print("\n\nCommand Line Login Manager\nAuthor: Alexander Oh | License: MIT Open Source\n\nNote: Do not use this login manager, this is a demonstration of learning for a AP Computer Science final. I am not responible for dumb mistakes.\n\n| New Login (n) | Login List (l) |")
    prompt = input("> ")
    if(prompt == "n"):
        print("\n\n[NEW LOGIN]")
        loginName = input("| Login Name: ")
        userName = input("| Username: ")
        passWord = input("| Password: ")
        
    elif(prompt == "l"):
        return "list"
    else: 
        return "repeat"
