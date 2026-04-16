###################################################################################
#  File Name   :   MultiTaskingThread8.py  
#
#  Description :  use of args keyword   
#              
#  Accept      :      
#  Return      :     
# 
#  Author      :     Rutuja Bharat varal
#  Date        :     17/01/2026
#
###################################################################################
import threading
 
def Display(No):
    print("Inside Display : ",No)
 
def main():
    t = threading.Thread(target=Display,args=(11,))
    t.start()
    
    
if __name__=="__main__":
        main()      
    
