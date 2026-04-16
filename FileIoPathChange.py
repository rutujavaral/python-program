
###################################################################################
#  File Name   :     FileIOPathChange.py
#
#  Description :     change path of the file [Absolute,Relative]
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
    
    if(os.path.exists(FileName)):
        Ret=os.path.isabs(FileName)
        
        if(Ret==True):
            print("It is Absolute path")
            
        else:
            print("It is Relative path")
            NewPath = os.path.abspath(FileName)
            print("Updated path:",NewPath)
            
    else:
        print("There is no such file")        
        
    

if __name__=="__main__":
        main()