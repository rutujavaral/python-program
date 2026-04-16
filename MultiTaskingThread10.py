###################################################################################
#  File Name   :   MultiTaskingThread10.py  
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
 
def SumEven(No):
    sum=0
    for i in range(2,No+1,2):
        sum=sum+i
        
    print("Even sum is :",sum)
        
 
def main():
    SumEven(10)
    
    
if __name__=="__main__":
        main()      
    
