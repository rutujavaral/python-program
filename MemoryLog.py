# Command line input

import psutil
import sys
import os
import time

def CreateLog(FolderName):
    
    Ret=False
    
    Ret=os.path.exists(FolderName)
    if(Ret==True):
        Ret=os.path.isdir(FolderName)
        if(Ret==False):
           print("Unable to create folder")
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        return
    
    else:
        os.mkdir(FolderName)
        print("Directory for log files created sucessfully")
        print("Directory created")
    
    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName=os.path.join(FolderName,"Marvellous_%s.log" % timestamp)
    print(FileName)
    
    fobj=open(FileName,"w")
    
    print("CPU uasage :",psutil.cpu percent())
    
    mem = psutil.virtual_memory()
    print("RAM Usage : ",mem.percent)
    

def main():
    Border ="-"*50
    print(Border)
    print("-------Marvellous Platform Surveilance System-----")
    print(Border)

    if(len(sys.argv) ==2):
        if(sys.argv[1] =="--h"or sys.argv[1] =="--H"):
            print("This script is used to :")
            print("1 : Create automatic logs")
            print("2 : Executes peroidically")
            print("3 : Send mail with the log")
            print("4 : Store the information about process")
            print("5 : Store the information about CPU")
            print("6 : Store the information about RAM usage")
            print("7 : Store the information about Secondary storage")

        elif(sys.argv[1] =="--u"or sys.argv[1] =="--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    # python Demo.py 5 Marvellous
    elif(len(sys.argv) ==3):
        print("Inside Project logics")
        print("Time Interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])
        print("Press cntrl + c to stop the ecxection")
        
        schedule.every(int(sys).argv[1]).minutes
        
        CreateLog(sys.argv[2])
    
    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)

if __name__=="__main__":
        main()