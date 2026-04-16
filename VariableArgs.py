###################################################################################
#  File Name   :     VariableArgs.py
#
#  Description :     Arguments in python[variable no of arguments]
#              
#  Accept      :      
#  Return      :     
# 
#  Author      :     Rutuja Bharat varal
#  Date        :     04/01/2026
#
###################################################################################

def Addition(*No):
    print(No)
    print(type(No))  #TUPLE
    print(len(No))
    
    
        
def main():
    Addition(11,21,51,101)
   
   
    
if __name__=="__main__":
        main()