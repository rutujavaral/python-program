
###################################################################################
#  File Name   :     FileIORemove.py
#
#  Description :     delete the file 
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
       os.remove(FileName)
       print("File gets deleted") 
            
        
            
    else:
        print("There is no such file")        
        
    

if __name__=="__main__":
        main()