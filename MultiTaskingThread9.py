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
 
def Display(No1,No2,No3):
    print("Inside Display : ",No1,No2,No3)
 
def main():
    t = threading.Thread(target=Display,args=(11,21,51))
    t.start()
    
    
if __name__=="__main__":
        main()      
    
