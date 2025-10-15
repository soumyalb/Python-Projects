# Problem Statement:
# Often, we have a large number of files in a directory with names that do not follow a specific pattern or are not easy to understand. 
# Renaming each file manually can be time-consuming and error-prone. To solve this problem,
# we need a program that can rename a large number of files in bulk, based on a specified pattern.

# Question:
# Can you develop a Python program that takes a directory path and a pattern as input, 
# and renames all the files in the directory that match the pattern to a new name that follows the specified pattern?

import os
# print(os.listdir("largefiles_folder"))
def largefile_renamer(dir_path,pattern):
    lst = os.listdir(dir_path)
    for count,filename in enumerate(lst):
        if filename[-4:] == pattern:
            src = f'{dir_path}/{filename}'
            dst = f'{dir_path}/my_txt_file{count}'+pattern
            os.rename(src,dst)

largefile_renamer("largefiles_folder",".txt")

# Improved version:---------------------------------------

import os

def largefile_renamer(dir_path, extension):
    files = os.listdir(dir_path)
    
    for count, filename in enumerate(files):
        if filename.endswith(extension):
            src = os.path.join(dir_path, filename)
            dst = os.path.join(dir_path, f"my_file_{count}{extension}")
            
            if not os.path.exists(dst):  # Avoid overwriting
                os.rename(src, dst)
            else:
                print(f"Skipping {dst}, file already exists.")

# Example usage
largefile_renamer("largefiles_folder", ".txt")