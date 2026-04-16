###################################################################################
#  File Name   : TimeCalculation.py   
#
#  Description : factorial       
#              
#  Accept      :      
#  Return      :     
# 
#  Author      :     Rutuja Bharat varal
#  Date        :     17/01/2026
#
###################################################################################
import time

def factorial(No):
    Fact=1
    
    for i in range(1,No+1):
        Fact =Fact * i
        
    return Fact    
 
def main():
     
     Value= int (input("Enter Number :"))
     
     start_time=time.time()
     
     Ret=factorial(Value)
     
     end_time=time.time()
      
     print("Factorial is :",Ret) 
     
     print("Total execution time is :" ,end_time-start_time)
        
if __name__=="__main__":
        main()      
    
