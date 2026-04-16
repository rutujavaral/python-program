###################################################################################
#  File Name   :     Default.py
#
#  Description :     Default Argument in python
#              
#  Accept      :      
#  Return      :     
# 
#  Author      :     Rutuja Bharat varal
#  Date        :     04/01/2026
#
###################################################################################

def EmployeeInfo(Name="Gotya",Age=21,Salary=1000,City="Mumbai"):
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salary : ",Salary)
    print("City : ",City)
    
    
    
        
def main():
    #EmployeeInfo(Age=26,Name="Rahul",City="Pune",Salary=2000.50)   CORRECT
    EmployeeInfo()
    
   
    
if __name__=="__main__":
        main()