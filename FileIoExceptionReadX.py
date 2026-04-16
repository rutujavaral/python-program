
###################################################################################
#  File Name   :     FileIOExceptionReadX.py
#
#  Description :     Read the file 
#              
#  Accept      :      
#  Return      :     
# 
#  Author      :     Rutuja Bharat varal
#  Date        :     31/01/2026
#
###################################################################################
def main():
    
    try:
     fobj=open("Hello.txt","r")
     print("File gets Sucessfully opened")
     
     data=fobj.read(6)
     
     print("data from file is :",data)
     
     fobj.close()
     
    except FileNotFoundError:
        print("Unable to opened file as there is no such file") 
      
    finally:
        print("End of application")   
        
        
    
if __name__=="__main__":
        main()