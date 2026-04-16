
###################################################################################
#  File Name   :     FileIOPath.py
#
#  Description :     check path of the file [Absolute,Relative]
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
    
    Ret=os.path.isabs(FileName)
    
    if(Ret==True):
        print("It is Absolute path")
        
    else:
        print("It is Relative path")
        
    
    

if __name__=="__main__":
        main()