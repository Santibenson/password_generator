import secrets
import string


def passwordGen():
    letters = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation
    alpha = letters + digits + special_char
    strNum = letters + digits

    pwlen = int(input("What's the length of the password? > "))
    needSChar = input("Do you need special characters? (Y/N) > ").lower()

    pwd = ""
    if needSChar == "y":
        for i in range(pwlen):
            pwd += "".join(secrets.choice(alpha))
    else:
        for i in range(pwlen):
            pwd += "".join(secrets.choice(strNum))
    print(pwd)

passwordGen()
