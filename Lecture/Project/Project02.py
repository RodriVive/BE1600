def main():
    print("Menu\n---------------\n",
    "1. Look up an email address\n",
    "2. Add a new name and email address\n",
    "3. Change an existing email address\n",
    "4. Delete a name and email address\n",
    "5. Quit the program\n")
    user = input("Enter your choice: ")
    userChoice(user)

def userChoice(choice):
    if choice == "1":
        lookUp()
    elif choice == "2":
        newEmail()
    elif choice == "3":
        changeEmail()
    elif choice == "4":
        deleteInfo()
    elif choice == "5":#Ends the program
        print("Information saved.")
    else:#Calls on the function again if the input is invalid
        print("** invalid option")
        user = input("Please enter a valid option: ")
        userChoice(user)

def lookUp():
    user = input("Enter a name: ")
    nameInfo = open("Lecture/Project/data.txt", 'r')
    infoList = nameInfo.readlines()
    dict = {}
    for i in infoList:
        info = i.split("!")
        dict[info[0]] = info[1]
    userInfo = open("Lecture/Project/data.txt", 'a')
    try:
        print("Name: ", user)
        print("Email: ", dict[user])
    except:
        print("That specified name was not found.\n")
    finally:
        main()

def newEmail():
    name = input("Enter name: ")
    email = input("Enter email address: ")
    nameInfo = open("Lecture/Project/data.txt", 'r')
    infoList = nameInfo.readlines()
    dict = {}
    for i in infoList:
        info = i.split("!")
        dict[info[0]] = info[1]
    userInfo = open("Lecture/Project/data.txt", 'a')
    if name not in dict:
        userInfo.write(name+"!"+email+"\n")
        userInfo.close()
    else:
        print("That name already exists")
    print("\n\n")
    main()

def changeEmail():
    user = input("Enter a name: ")
    email = input("Enter new adress: ")
    nameInfo = open("Lecture/Project/data.txt", 'r')
    infoList = nameInfo.readlines()
    dict = {}
    for i in infoList:
        info = i.split("!")
        dict[info[0]] = info[1]
    userInfo = open("Lecture/Project/data.txt", 'w')
    if user in dict:
        dict[user] = email
        infoList[list(dict.keys()).index(user)] = user + "!" + email + "\n"
        print(infoList)
        for i in infoList:
            userInfo.write(i)
        userInfo.close()
        print("Information updated.\n")
    else:
        print("That specified name was not found.\n")
    
    main()

def deleteInfo():
    user = input("Enter a name: ")
    nameInfo = open("Lecture/Project/data.txt", 'r')
    infoList = nameInfo.readlines()
    dict = {}
    for i in infoList:
        info = i.split("!")
        dict[info[0]] = info[1]
    userInfo = open("Lecture/Project/data.txt", 'w')
    try:
        infoList.pop(list(dict.keys()).index(user))
        print(infoList)
        for i in infoList:
            userInfo.write(i)
        userInfo.close()
        print("Information deleted.\n")
    except:
        print("That specified name was not found.\n")
    finally:
        main()

main()