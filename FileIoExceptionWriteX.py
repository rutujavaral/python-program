
###################################################################################
#  File Name   :     FileIOExceptionWriteX.py
#
#  Description :     write the file 
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
     fobj=open("Hello.txt","w")
     print("File gets Sucessfully opened")
     
     fobj.write(" Jay Ganesh Marvellous...")
     
     fobj.close()
     
    except FileNotFoundError:
        print("Unable to opened file as there is no such file") 
      
    finally:
        print("End of application")   
        
        
    
if __name__=="__main__":
        main()