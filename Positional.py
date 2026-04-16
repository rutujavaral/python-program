###################################################################################
#  File Name   :     Positional.py
#
#  Description :     Arguments in python[positional]
#              
#  Accept      :      
#  Return      :     
# 
#  Author      :     Rutuja Bharat varal
#  Date        :     04/01/2026
#
###################################################################################

def Display(A,B,C,D):
    print(A,B,C,D)
    
        
def main():
    # Display(10,20)             NOT ALLOWED-less arguments
    # Display(10,20,30,40,50)    NOT ALLOWED-extra arguments
    Display(10,20,30,40)         #ALLOWED
   
    
if __name__=="__main__":
        main()