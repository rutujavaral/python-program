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
import time
 
def SumEven(No):
    sum=0
    for i in range(2,No+1,2):
        sum=sum+i
        
    print("Even sum is :",sum)
 
def SumOdd(No):
    sum=0
    for i in range(1,No+1,2):
        sum=sum+i  
    print("odd sum is :",sum)         
 
 
def main():
    start_time=time.time()
    
    SumEven(1000000000)
    SumOdd(1000000000)
    
    end_time=time.time()
    
    print("Time required:",end_time-start_time)
    
    
    
if __name__=="__main__":
        main()      
    
