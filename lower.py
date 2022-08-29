import os
import core

def run(source_path):
    confirm = ""
    print("")
    confirm = input("Do you confirm to convert to lower case (y/n)? ").lower()
    
    if confirm == "y":        
        item_list = os.listdir(source_path)
        full_path = list()
        for item in item_list:
            full_path.append(source_path + "/" + item)
        file_list = list()
        renamed_list = list()
        for item in full_path:
            if os.path.isfile(item):
                file_list.append(item)
                renamed_list.append(item[:item.rfind("/")] \
                                    + item[item.rfind("/"):item.rfind(".")].lower()\
                                        + item[item.rfind("."):])
    
        core.rename(file_list, renamed_list, exist_test = False)
    else:
        print("No files have been renamed!")