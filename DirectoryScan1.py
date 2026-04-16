
###################################################################################
#  File Name   :     DirectoryScan1.py
#
#  Description :     
#              
#  Accept      :      
#  Return      :     
# 
#  Author      :     Rutuja Bharat varal
#  Date        :     31/01/2026
#
###################################################################################
import os

def main():
    DirectoryName=input("Enter the name of directory")

    print("Contents of the directory are:") 
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Foder Name :",FolderName)
        
        for subf in SubFolderName:
            print("SubFolder Name:",subf)
            
        for fname in FileName:
            print("File Name:",fname)
                   

if __name__=="__main__":
        main()