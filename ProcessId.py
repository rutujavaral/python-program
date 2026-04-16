###################################################################################
#  File Name   :     processId.py
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
import os

def main():
    print("PID of running process is : ",os.getpid())
    print("PID of parent process is :",os.getppid())
    
if __name__=="__main__":
        main()