import random
from math import *

def custom_hash(salted_password):
    length = len(salted_password)
    hashed = 0
    prime1 = 37
    prime2 = 29
    for index in range(length):
        rev_index = length - index - 1
        char = salted_password[rev_index]     
        char_value = ord(char)

        hashed = hashed + (length * rev_index * prime1 + char_value * (index + prime2) + char_value % prime1) % (2 ** 32)


    return hex(hashed)


def custom_salt(length = 8):
    universal_set = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()"
    uni_length = len(universal_set)
    salt = ""
    for i in range(length):
        salt = salt + universal_set[floor(random.random() * uni_length)]
    
    return salt

def positionof(user_username, username_list):
    i = 0
    flag = -1
    for username in username_list:
        if user_username == username:
            return (i)
        i = i + 1
    return flag

username_list = []
salt_list = []
hashed_salted_password_list = []

print("Welcome")
print("\n")
print("Press any other key apart from given options to exit the program")
print("\n\n")
print("1. Already a user? Login!")
print("2. New user? Sign Up!")
user_choice = input("Enter your choice : ")
print("\n")

while user_choice == "1" or user_choice == "2":
    if user_choice == "1":
        user_username = input("Username : ")
        user_password = input("Password : ")

        position = positionof(user_username, username_list)

        if position == -1:
            print("Incorrect Username or Password")
        else:
            salt = salt_list[position]
            salted_user_password = salt + user_password
            hashed_salted_user_password = custom_hash(salted_user_password)

            if hashed_salted_user_password == hashed_salted_password_list[position]:
                print("Successful Login!")
            else:
                print("Incorrect Username or Password")
        print("\n\n")
            
    else:
        user_username = input("Enter Username : ")

        while positionof(user_username, username_list) != -1:
            print("Sorry! Username already taken. Please select another username.")
            user_username = input("Enter Username : ")

        user_password = input("Enter Password : ")

        username_list.append(user_username)
        salt = custom_salt()
        salted_user_password = salt + user_password
        hashed_salted_user_password = custom_hash(salted_user_password)

        salt_list.append(salt)
        hashed_salted_password_list.append(hashed_salted_user_password)

        print("Successfully Registered!")
        print("\n\n")
            

    print("1. Already a user? Login!")
    print("2. New user? Sign Up!")
    user_choice = input("Enter your choice : ")
    print("\n")

print("Thank You")
