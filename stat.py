import sys
import os

def display_stat(filename) :
    
    print("File Size : ")
    print(os.path.getsize(filename))
    print("File Modification date : ")
    print(os.path.getmtime(filename))
    print("File Creation data : ")
    print(os.path.getctime(filename))
    
    #using stat
    stats = os.stat(filename)
    print("File Size : ")
    print(stats.st_size)
    print("File Modification date : ")
    print(stats.st_mtime)
    print(stats.st_uid)
    print("GUI ID :")
    print(stats.st_gid)
    print("Inode Number : ")
    print(stats.st_ino)
    

display_stat("C:/xampp/htdocs/Test/test1.txt")