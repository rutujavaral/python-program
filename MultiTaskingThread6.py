###################################################################################
#  File Name   :   MultiTaskingThread5.py  
#
#  Description :      
#              
#  Accept      :      
#  Return      :     
# 
#  Author      :     Rutuja Bharat varal
#  Date        :     17/01/2026
#
###################################################################################
import threading

def Display():
    
    for i  in range(10):
        print("Inside Display function:",threading.get_ident())
       
    
 
def main():
    print("Inside main:",threading.get_ident())
    
    t1=threading.Thread(target=Display)
    t1.start()
   
    
    t2=threading.Thread(target=Display)
    t2.start()
    
    t1.join()
    t2.join()
    
    print("End of main")
    
if __name__=="__main__":
        main()      
    
