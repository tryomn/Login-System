import hashlib
import os


def clear(): return os.system('clear')


def main():
    clear()
    print("MAIN MENU")
    print("_____________")
    print()
    print("1 - Register")
    print("2 - Login")
    print()

    while True:
        print()
        userChoice = input("Choose an Option: ")
        if userChoice in ['1', '2']:
            break
    if userChoice == '1':
        Register()

    else:
        login()


def Register():
    clear()
    print("_____________")
    print()

    while True:
        userName = input('Enter your name: ').title()
        if userName != '':
            break
    userName = sanitizeName(userName)

    while True:
        userPassword = input("Enter Your Password: ")
        if userPassword != '':
            break

    while True:
        confirmPassword = input("Confirm Your Password: ")
        if confirmPassword == userPassword:
            break
        else:
            print("Password Mismatch")
            print()
    if userAlreadyExist(userName, userPassword):
        while True:
            print()
            error = input(
                "You Are Already Registered.\n\nPress(T) To Try Again:\nPress(L) To Login: ").lower()
            if error == 't':
                Register()
                break
            elif error == 'l':
                login()
                break
    addusersInfo([userName, hash_password(userPassword)])

    print()
    print("Registered!")


def login():
    clear()
    print("LOGIN")
    print("_____________")
    print()

    userInfo = {}
    with open('password.txt', 'r') as file:
        for line in file:
            line = line.split()
            userInfo.update({line[0]: line[1]})

    while True:
        userName = input("Enter Your Name: ").title()
        userName = sanitizeName(userName)
        if userName not in userInfo:
            print("You Are Not Registered")
            print()
        
        else:
            break

    while True:
        userPassword = input("Enter Your Password: ")
        if not check_password_hash(userPassword, userInfo[userName]):
            print("Incorrect Password")
            print()
            
        else:
            break

    print()    
    print(f"You've successfully logged in.\n Welcome {userName}")


def addusersInfo(userInfo: list):
  with open('password.txt', 'w') as file:
    for info in userInfo:
      file.write(info)
      file.write(' ')
    file.write('\n')


def userAlreadyExist(userName, userPassword):
    userPassword = hash_password(userPassword)
    userInfo = {}
    with open('password.txt', 'r') as file:
        for line in file:
            line = line.split()
            if line[0] == userName and line[1] == userPassword:
                userInfo.update({line[0]: line[1]})
    if userInfo == {}:
        return False
    return userInfo[userName] == userPassword


def sanitizeName(userName):
    userName = userName.split()
    userName = '_'.join(userName)
    return userName


def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_password_hash(password, hash):
    return hash_password(password) == hash
    print(hash)


if __name__ == '__main__':
    main()