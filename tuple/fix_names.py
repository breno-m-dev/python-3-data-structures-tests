# this script was made to rename all 
# files I misspeled the word "tuple" as "tupple"

import os

FOLDER_PATH = "D:/programacao/python learning/python-3-data-structures/tuple"  

for filename in os.listdir(FOLDER_PATH):
    #print(filename)
    if "tupple" in filename:
        old_path = FOLDER_PATH + "/" + filename
        new_path = FOLDER_PATH + "/" + filename.replace("tupple","tuple")
        os.rename(old_path,new_path)
        print(filename+" renamed")