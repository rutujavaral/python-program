
###################################################################################
#  File Name   :     FileIOExceptionAppend.py
#
#  Description :     Append the file 
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
     fobj=open("Hello.txt","a")
     print("File gets Sucessfully opened")
     
     fobj.write("Python Automation")
     
     fobj.close()
     
    except FileNotFoundError:
        print("Unable to opened file as there is no such file") 
      
    finally:
        print("End of application")   
        
        
    
if __name__=="__main__":
        main()