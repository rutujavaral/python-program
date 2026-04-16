###################################################################################
#  File Name   :   MultiTaskingThread4.py  
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
    print("Inside Display function:",threading.get_ident())
    for i  in range(100):
        print("Inside Display")
    
 
def main():
    print("Inside main:",threading.get_ident())
    
    t=threading.Thread(target=Display)
    t.start()
    t.join()
    
    print("End of main")
    
if __name__=="__main__":
        main()      
    
