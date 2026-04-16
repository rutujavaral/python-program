
###################################################################################
#  File Name   :     FileIOExceptionReadSeekX.py
#
#  Description :     read [Seek] the file 
#              
#  Accept      :      
#  Return      :     
# 
#  Author      :     Rutuja Bharat varal
#  Date        :     31/01/2026
#
###################################################################################
#Seek(kuthe,kuthun)
#kuthun:0/1/2
#0:starting
#1:Current
#2:End
def main():
    
    try:
     fobj=open("Hello.txt","r")
     print("File gets Sucessfully opened")
     
     print("Current offset is :",fobj.tell()) #0
     
     fobj.seek(7,0)
     
     print("Current offset is :",fobj.tell()) #7
     
     
     data=fobj.read(10)
     
     print("Current offset is :",fobj.tell()) #17
     
     print("data from file is :",data)
     
     fobj.close()
     
    except FileNotFoundError:
        print("Unable to opened file as there is no such file") 
      
    finally:
        print("End of application")   
        
        
    
if __name__=="__main__":
        main()