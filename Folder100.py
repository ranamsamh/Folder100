import os
import art
from colorama import Fore

title = art.text2art("Folder 100")
print(Fore.BLUE, "-------------------------------------------------------------")
print(Fore.MAGENTA, title)
print(Fore.LIGHTBLACK_EX, "Version 1.0")
print(Fore.WHITE, "Created by: Rana Aboulsamh")
print(Fore.BLUE, "-------------------------------------------------------------")


path = input("Enter the directory where your new folder(s) will live: ")
numOfSubjects = int(input("How many subjects do you have?: "))

subjects = []
for i in range(1,numOfSubjects+1):
    subjects.append(input(f"Enter subject {i}: "))


while True:
    subfolder_condition = input("Would you like to add sub-folders to your subjects? (y/n):")

    if subfolder_condition not in ("y", "yes", "n", "no"):
        print("Error! Please Try Again")
        continue
    else:
        if subfolder_condition == "y" or subfolder_condition == "yes":
            numofSubfolder = int(input("How many subfolders would you like?: "))
            subfolders_list = []
            for j in range(1,numofSubfolder+1):
                subfolders_list.append(input(f"Enter name of subfolder {j}: "))

            for sub in subjects:
                for folder in subfolders_list:
                    os.makedirs(f"{path}\\{sub}\\{folder}")
            break

        elif subfolder_condition == "n" or subfolder_condition == "no":
            for sub in subjects:
                os.makedirs(f"{path}\\{sub}")
            break

print("\nYour new files have been created in the directory you requested")
print("Enjoy :)")