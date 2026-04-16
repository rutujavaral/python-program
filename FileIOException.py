
###################################################################################
#  File Name   :     FileIOException.py
#
#  Description :     open the file 
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
     open("Demo.txt")
     print("File gets Sucessfully opened")
     
    except FileNotFoundError:
        print("Unable to opened file as there is no such file") 
      
    finally:
        print("End of application")   
        
    
if __name__=="__main__":
        main()