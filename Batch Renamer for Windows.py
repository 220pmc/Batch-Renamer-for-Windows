# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 05:15:41 2022

@author: User
"""
#import required files and modules
import menu

def main():
    menu.Title().update_cmd_title()
    menu.Title().title_display()
    menu.Description().description_display()
    menu.MenuItems().menu_display()
    menu_items = menu.MenuItems().get_menu_dict()
    user_input = menu.OptionInput().get_user_input()
    source_path = menu.OptionInput().get_source_path()
    
    # invoke corresponding rename option
    option = menu_items[user_input]
    if option == "Add prefix":
        import prefix
        prefix.run(source_path)
    elif option == "Add suffix (Before extension)":
        import suffix_before_extension
        suffix_before_extension.run(source_path)
    elif option == "Add suffix (After extension)":
        import suffix_after_extension
        suffix_after_extension.run(source_path)
    elif option == "Convert to upper case":
        import upper
        upper.run(source_path)
    elif option == "Convert to lower case":
        import lower
        lower.run(source_path)
    elif option == "Convert to title case":
        import title
        title.run(source_path)
    """
    Under Development
    elif option == "Replace the first occurance of a word":
        import replace
        first_replace.run(source_path)
    #elif option == "Replace the first occurance of a word":
        import replace
        last_replace.run(source_path)
    """
    
    print("Press enter to quit the program")
    input()
    
    
    

main()
