
###################################################################################
#  File Name   :     DirectoryScan2.py
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

def DirectoryScanner(DirectoryName):
    
    
   
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Foder Name :",FolderName)
        
        for subf in SubFolderName:
            print("SubFolder Name:",subf)
            
        for fname in FileName:
            print("File Name:",fname)

    print("Contents of the directory are:") 
    

def main():
    
     DirectoryName=input("Enter the name of directory")
     
     DirectoryScanner=(DirectoryName)
    
                   

if __name__=="__main__":
        main()