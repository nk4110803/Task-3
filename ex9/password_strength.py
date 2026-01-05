import re

def check_password_strength(password):
    if not re.search(r'[a-z]', password) :
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    if len(password) < 8:
        return False
    if any(password.count(char) > 2 for char in password):
        return False
    for i in range(len(password) - 2):
        if ord(password[i])+1 == ord(password[i + 1]) and ord(password[i + 1])+1 == ord(password[i + 2]):
            return False
    return True

while True:
    pwd = input("Enter a password to check its strength: to get out type 'exit'\n")
    if pwd == "exit":
        print("exiting...")
        break
    if check_password_strength(pwd):
        print("Strong password")
    else:
        print("Weak password")