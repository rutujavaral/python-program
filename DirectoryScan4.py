
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

def DirectoryScanner(DirectoryName="Marvellous"):
    
    Ret=os.path.exists(DirectoryName)
    
    if(Ret==False):
        print("There is no such Directory:")
        return
    Ret=os.path.isdir(DirectoryName)
    
    if(Ret==False):
        print("Unable to scan as its not aDirectory")
        return
        
    print("Contents of the directory are:") 
   
    
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