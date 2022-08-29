# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:40:23 2022

@author: User
"""

import os
import time

def rename(file_list, renamed_list, exist_test):
    log = open("log.txt", "a")
    success = ""
    time_now = time.localtime()
    log.write("=" * 50)
    log.write("\n")
    
    for i in range(len(file_list)):
        if os.path.exists(renamed_list[i]) and exist_test:
            log.write("{} - ".format(time.strftime("%H:%M:%S", time_now)))
            log.write("\"{}\" exists. File has not been renamed\n\n".format(renamed_list[i]))
            print("\n\"{}\" exists.\nFile has not been renamed.".format(renamed_list[i]))
        else:
            os.renames(file_list[i], renamed_list[i])
            success += "{} - ".format(time.strftime("%H:%M:%S", time_now))
            success += "\"" + file_list[i] + "\"" + "\nhas been renamed to\n\"{}\" successfully!\n\n".format(renamed_list[i])
            print("\n\"" + file_list[i] + "\"" + "\nhas been renamed to\n\"{}\" successfully!".format(renamed_list[i]))
    
    log.write(success)
    log.close()
