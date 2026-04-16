
###################################################################################
#  File Name   :     FileIOFunctions.py
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
       fobj=open(FileName,"r")
       
       print(fobj.name)                  #Demo.txt
       print(fobj.mode)                   #r
       print(fobj.closed)                 #false
       
       fobj.close()
                  
    else:
        print("There is no such file")  
        print(fobj.closed)                    #True
              
        
    

if __name__=="__main__":
        main()