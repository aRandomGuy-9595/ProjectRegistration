from datetime import datetime
import random
from random import randrange
from os import system
import tkinter as tk
from getpass import getpass

file_path = "E:/Skul/Storage/data.txt"

def searching(useraidi):
    if len(useraidi) == 0:
        print("Please enter a valid username.")
        return True
    if useraidi in id_data:
        print(f"""
----------
Data Found
----------
Name: {useraidi}
Reg ID: {id_data[useraidi]["regid"]}
Registration time: {id_data[useraidi]["date"]}
Password: {id_data[useraidi]["passw"]}
                """)
        return True
    else:
        print("--------------")
        print("Data not found")
        print("--------------")
        return True

def searchingg(useraidi):
    if len(useraidi) == 0:
        print("Please enter a valid username.")
        return True
    if useraidi in id_data:
        print(f"""
----------
Data Found
----------
Name: {useraidi}
Reg ID: {id_data[useraidi]["regid"]}
Registration time: {id_data[useraidi]["date"]}
Password: {id_data[useraidi]["passw"]}
                """)
        return False
    else:
        print("--------------")
        print("Data not found")
        print("--------------")
        return True

def searching_guest(useraidi):
    if useraidi in id_data:
        print(f"""
----------
Data Found
----------
Name: {useraidi}
Registration time: {id_data[useraidi]["date"]}
                """)
        return True
    else:
        print("--------------")
        input("Data not found, press ENTER to continue")
        print("--------------")
        input_awal()

def searching_sendiri(useraidi):
    if useraidi in id_data:
        print(f"""
----------
Data Found
----------
Name: {useraidi}
Registration time: {id_data[useraidi]["date"]}
                """)
        return True
    else:
        print("--------------")
        input("Data not found, press ENTER to finish")
        print("--------------")
        input_awal()

def print_header(msg):
	system("cls")
	print(msg)

def hapus_sendiri():
    for useraidi in list(id_data):
        plox = input("Enter your name: ").title()
        bruh = searching_guest(plox)
        if bruh:
            confirmation = getpass("""
Please confirm your password to delete your data
(For security reasons, your password will not show here) : """)
            if confirmation == id_data[plox]["passw"]:
                print("Registration ID " + id_data[plox]["regid"] + " deleted.")
                del id_data[plox]
                print("Data deleted.")
                input("Press ENTER to finish")
                print("----------------------------------")
                input_awal()
            else:
                print("Wrong password.")
                input("Press ENTER to finish")
                print("----------------------------------")
                input_awal()

def cari_sendiri():
    for useraidi in list(id_data):
        plox = input("Enter your name: ").title()
        bruh = searching_sendiri(plox)
        if bruh:
            confirmation = getpass("""
Please confirm your password to see your data
(For security reasons, your password will not show here) : """)
            if confirmation == id_data[plox]["passw"]:
                print("Your registration ID : " + id_data[plox]["regid"])
                input("Press ENTER to finish")
                print("----------------------------------")
                system("cls")
                input_awal()
            else:
                print("Wrong password.")
                input("Press ENTER to finish")
                print("----------------------------------")
                input_awal()

id_data = {
}

id_admin = {
    "Malvin" : {
        "pasw" : "12345"
    },
    "Dummy" : {
        "pasw" : "abcde"
    }
}

def input_awal():
    system("cls")
    print("""
Please select an option.
[1] - To get your ticket number.
[2] - To delete your ticket number.
[3] - To find your ticket number.
[4] - Admin bench
            """)
    bleh = input("Choice? : ")
    print("----------------------------------")
    if bleh == "1":
        print("Get your ticket number here")
        name = input("Name : ").title()
        passw = getpass("""
Create a password
(For security reasons, your password will not show here) : """)
        passw2 = getpass("""
Confirm your password
(For security reasons, your password will not show here) : """)
        if len(name) == 0:
            input("Please enter a valid name.")
        else:
            if passw == passw2:
                system("cls")
                tanggal = datetime.now().replace(microsecond = 0)
                registrationid = randrange(100000000, 999999999)
                regid = name[0].upper() + name[-1].upper() + str(registrationid)
                print("Your registration ID:",regid)
                print("Date and time:",tanggal)
                print("----------------------------------")
                id_data[name] = {
                                    "regid" : regid,
                                    "date" : tanggal,
                                    "passw" : passw
                        }
                input("Press ENTER to finish")
                print("----------------------------------")
                input_awal()
            else:
                print("Your password and confirmation does not match.")
                input("Press ENTER to finish")
                print("----------------------------------")
    elif bleh == "2":
        if len(id_data) == 0:
            input("No IDs yet, press ENTER to finish")
            print("----------------------------------")
            input_awal()
        else:
            hapus_sendiri()
    elif bleh == "3":
        if len(id_data) == 0:
            input("No IDs yet, press ENTER to finish")
            print("----------------------------------")
            input_awal()
        else:
            cari_sendiri()
    elif bleh == "4":
        admin_login()
    else:
        print("Invalid input.")
        input("Press ENTER to finish")
        print("----------------------------------")

def confirmations():
    print("""
----------------------------
[1] - Log out
[2] - Go back to ADMIN BENCH
                """)
    biji = input("Choice?: ").upper()
    if biji == "1":
        print("----------------------------------")
        input_awal()
    elif biji == "2":
        print("----------------------------------")
        system("cls")
        admin_login()
    else:
        print("Invalid input.")
        input("Press ENTER to finish")
        print("----------------------------------")

def admin_login():
    user = input("Enter your User ID : ").title()
    pasw = getpass("""
Your password?
(For security reasons, your password will not show here) : """)
    if user in id_admin:
        if pasw == id_admin[user]["pasw"]:
            stahp = False
            while not stahp:
                system("cls")
                menu = f"""
Admin Bench - Welcome back, {user}.
[1] - To see registered IDs.
[2] - To search available data(s).
[3] - To delete registered data(s).
[4] - Export data and overwrite.
[5] - Log out.
                        """
                print(menu)
                user_input = input("Choice: ")
                print("----------------------------------")
                if user_input == "1":
                    print_header("Registered IDs")
                    print("----------------------------------")
                    if len(id_data) == 0:
                        print("No IDs yet.")
                        input("Press ENTER to finish")
                        print("----------------------------------")
                    else:
                        for useraidi in id_data:
                                name = useraidi
                                regid = id_data[useraidi]["regid"]
                                regdate = id_data[useraidi]["date"]
                                passw = id_data[useraidi]["passw"]
                                print(f"""
Name: {name}
Reg ID: {regid}
Registration time: {regdate}
Password: {passw}
                                        """)
                        input("Press ENTER to finish")
                        print("----------------------------------")
                elif user_input == "2":
                    if len(id_data) == 0:
                        print("No IDs yet.")
                        input("Press ENTER to finish")
                        print("----------------------------------")
                    else:
                        print_header("Find data")
                        bjir = input("Name: ").title()
                        result = searching(bjir)
                        input("Press ENTER to finish")
                        print("----------------------------------")
                elif user_input == "3":
                    if len(id_data) == 0:
                        print("No IDs yet.")
                        input("Press ENTER to finish")
                        print("----------------------------------")
                    else:
                        plox = input("Enter name of whose data you want to delete: ").title()
                        bruh = searchingg(plox)
                        if bruh == False:
                            confirmation = input(f"Are you sure to delete {plox}'s data? This action CANNOT be undone. (Y/N)").upper()
                            if confirmation == "Y":
                                del id_data[plox]
                                print("Data deleted.")
                                input("Press ENTER to finish")
                                print("----------------------------------")
                            else:
                                print("Cancelled.")
                                input("Press ENTER to finish")
                                print("----------------------------------")
                        else:
                            input("Press ENTER to finish")
                            print("----------------------------------")
                elif user_input == "4":
                    if len (id_data) == 0:
                        print("No IDs yet.")
                        input("Press ENTER to finish")
                        print("----------------------------------")
                    else:
                        mode = "w"
                        for useraidi in id_data:
                                    name = useraidi
                                    regid = id_data[useraidi]["regid"]
                                    regdate = id_data[useraidi]["date"]
                                    passw = id_data[useraidi]["passw"]
                                    append_data = f"""
Name: {name}
Reg ID: {regid}
Registration time: {regdate}
Password: {passw}
                                        """
                                    with open(file_path, mode) as file:
                                        file.write(append_data)
                                        print("Export successful.")
                                        input("Press ENTER to finish")
                                        print("----------------------------------")
                elif user_input == "5":
                    input_awal()
                else:
                    print("Invalid input.")
                    input("Press ENTER to finish")
                    print("----------------------------------")
        else:
            print("Login failed. Username or password may be wrong.")
            input("Press ENTER to finish")
            print("----------------------------------")
            input_awal()
    else:
        print("Login failed. Username or password may be wrong.")
        input("Press ENTER to finish")
        print("----------------------------------")
        input_awal()

    



stop  = False

while not stop:
    input_awal()
