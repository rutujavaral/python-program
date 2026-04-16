
###################################################################################
#  File Name   :     FileIOFunctionsX.py
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
    
    FileName=input("Enter the name of File:")
    
    if(os.path.exists(FileName)):
       fobj=open(FileName,"w")
       
       print(fobj.readable())
       print(fobj.writable())
       print(fobj.seekable())
       
                  
    else:
        print("There is no such file")  
        print(fobj.closed)                    
              
        
    

if __name__=="__main__":
        main()