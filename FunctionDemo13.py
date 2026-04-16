###################################################################################
#  File Name   :     FunctionDemo13.py
#
#  Description :     Functions in python[Nested function]
#              
#  Accept      :      
#  Return      :     
# 
#  Author      :     Rutuja Bharat varal
#  Date        :     04/01/2026
#
###################################################################################

def Phoenix():
    print("Inside  Phoenix")
    
    def zara():
        print("Inside zara")
        
    zara()

        
def main():
    Phoenix()
   
    
if __name__=="__main__":
        main()