###################################################################################
#  File Name   :     KeyWord.py
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
    #POSITIONAL
    #EmployeeInfo("Rahul",26,20000.50,"Pune")      #CORRECT
    #EmployeeInfo(26,"Rahul","Pune",20000.50)      #WRONG
    
    #KEYWORD ARGUMENTS
    EmployeeInfo(Age=26,Name="Rahul",City="Pune",Salary=2000.50)  #CORRECT
    
    
   
    
if __name__=="__main__":
        main()