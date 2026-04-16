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
import os

def factorial(No):
    Fact=1
    
    for i in range(1,No+1):
        Fact =Fact * i
        
    return Fact    
 
def main():
     
     Value= int (input("Enter Number :"))
     
     Ret=factorial(Value)
      
     print("Factorial is :",Ret) 
        
if __name__=="__main__":
        main()      
    
