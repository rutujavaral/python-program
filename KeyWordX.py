###################################################################################
#  File Name   :     KeyWordX.py
#
#  Description :     Keyword Argument in python
#              
#  Accept      :      
#  Return      :     
# 
#  Author      :     Rutuja Bharat varal
#  Date        :     04/01/2026
#
###################################################################################

def EmployeeInfo(Name,Age,Salary,City):
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salary : ",Salary)
    print("City : ",City)
    
    
    
        
def main():
    
    #KEYWORD ARGUMENTS
    EmployeeInfo(Age=26,Name="Rahul",City="Pune",Salary=None)  #CORRECT
    
    
   
    
if __name__=="__main__":
        main()