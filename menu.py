import os

class Title:
    def __init__(self):
        self.__divider = "=" * 80
        self.__title = "Batch Renamer for Windows"
        self.__version = "v0.1"
        self.__author = "220pmc"
        
    def title_display(self):
        print(self.__divider)
        display_string = self.__title + " " + self.__version
        print("{:^80s}".format(display_string))
        print("{:>80s}".format("By " + self.__author))
        print(self.__divider, end = "\n\n")
        
    def get_title(self):
        return self.__title
    
    def get_version(self):
        return self.__version
    
    def update_cmd_title(self):
        os.system("title " + self.__title + " - " + self.__version)


class Description:
    def __init__(self):
        self.__description = "Thank you for using {}. This program is now under\n".format(Title().get_title()) \
            + "development. If you found any bugs or would like to make some suggestions,\n" \
                + "feel free to contact me on Github and leave a comment there.\n\n"\
                    + "My Github Page is: https://github.com/220pmc/\n"
    
    def get_description(self):
        return self.__description
    
    def description_display(self):
        print(self.__description)

class MenuItems:
    def __init__(self):
        self.__menu_items = dict()
        self.__menu_items[1] = "Add prefix"
        self.__menu_items[2] = "Add suffix (Before extension)"
        self.__menu_items[3] = "Add suffix (After extension)"
        self.__menu_items[4] = "Convert to upper case"
        self.__menu_items[5] = "Convert to lower case"
        self.__menu_items[6] = "Convert to title case"
        #self.__menu_items[7] = "Replace the first occurance of a word"
        #self.__menu_items[8] = "Replace the last occurance of a word"
        
    def get_menu_items(self):
        return self.__menu_items.values()
        
    def get_menu_num(self):
        return self.__menu_items.keys()
    
    def get_menu_dict(self):
        return self.__menu_items
    
    def menu_display(self):
        print("=" * 25)
        print("{:^25s}".format("Menu"))
        print("=" * 25)
        print()
        for i in range(1, len(self.__menu_items.values()) + 1):
            print(" {}.".format(i), self.__menu_items[i])
        print()
            
class OptionInput:
    def __init__(self):
        self.__input_message = "Please select option: "
        self.__confirm_message = "Do you confirm to proceed (y/n)? "
        self.__path_message = "Please enter your source folder path (without qoutes): "
        self.__user_input = 0
        self.__source_path = ""
        self.__confirmation = ""
        
    def confirmation(self):
        self.__confirmation = input(self.__confirm_message).lower()
        
    def get_user_input(self):
        try:
            self.__user_input = int(input(self.__input_message))
        except:
            pass
        finally:
            self.confirmation()
        
        while not (1 <= self.__user_input <= len(MenuItems().get_menu_items())) \
            or self.__confirmation != "y":
                try:
                    self.__user_input = int(input(self.__input_message))
                except:
                    pass
                finally:
                    self.confirmation()
        return self.__user_input
    
    def get_source_path(self):
        self.__source_path = input(self.__path_message)
        self.__source_path = self.__source_path.replace("\\", "/")
        self.confirmation()
        while not os.path.exists(self.__source_path) \
            or self.__confirmation != "y":
                self.__source_path = input(self.__path_message)
                self.__source_path = self.__source_path.replace("\\", "/")
                self.confirmation()
        return self.__source_path