import os
import core

def run(source_path):
    invalid_char = "\\/:*?\"<>|"
    valid = True
    confirm = ""
    print("")
    print("Please remember \"\\/:*?\"<>|\" cannot be included in a file name.")
    prefix = input("Enter a prefix: ")
    confirm = input("Do you confirm to proceed (y/n)? ").lower()
    for char in prefix:
        if char in invalid_char:
            valid = False
            print("Warning-1st")
            break
    while not valid or confirm != "y":
        prefix = input("Enter a prefix: ")
        confirm = input("Do you confirm to proceed (y/n)? ").lower()
        valid = True
        for char in prefix:
            if char in invalid_char:
                valid = False
                print("Warning - loop")
                break
            
    item_list = os.listdir(source_path)
    full_path = list()
    for item in item_list:
        full_path.append(source_path + "/" + item)
    file_list = list()
    renamed_list = list()
    for item in full_path:
        if os.path.isfile(item):
            file_list.append(item)
            renamed_list.append(item[:item.rfind("/") + 1] + prefix + item[item.rfind("/") + 1:])

    core.rename(file_list, renamed_list, exist_test = False)