
###################################################################################
#  File Name   :     FileIOExist.py
#
#  Description :     check Existance of the file 
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
    
    FileName=input("Enter the name of File:")
    
    Ret=os.path.exists(FileName)
    
    if (Ret==True):
        fobj=open(FileName,"r")
        print("File gets Sucessfully opened")
    else:
        print("There is no such file")
       
    
    
    
        
        
    
if __name__=="__main__":
        main()