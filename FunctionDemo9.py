###################################################################################
#  File Name   :     FunctionDemo9.py
#
#  Description :     Functions in python[One function can call another function]
#              
#  Accept      :      
#  Return      :     
# 
#  Author      :     Rutuja Bharat varal
#  Date        :     04/01/2026
#
###################################################################################

def fun():
     print("Inside fun")

def gun():
    print("Inside gun")
        
def main():
    fun()
    gun()
   
    
if __name__=="__main__":
        main()