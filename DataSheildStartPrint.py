# Command line input


import sys
import os
import time
import schedule
import shutil

def BackupFiles(Source,Destination):
    copied_files=[]
    
    print(" creating the backup folder for bakup process")
    
    os.makedirs(Destination,exist_ok=True)
    
    for root , dirs,files in os.walk(Source):
        for file in files:
            src_path=os.path.join(root,file)
            
            relative=os.path.realpath(src_path,Source)
            dest_path=os.path.join(Destination,relative)
            
            os.makedirs(os.path.dirname(dest_path),exist_ok=True)
    
    #copy the files if its new
    
    shutil.copy2(src_path,dest_path)
    copied_files.append(relative)
    
    return copied_files    
    
    pass

def MarvellousDataSheildStart(Source="Data"):
    BackupName="MarvellousBackup"
    
    print("Backup process statrtd sucesfully at ",time.ctime())
    
    files=BackupFiles(Source,BackupName)
    print("report about the backup")
    
    for name in files:
        print(name)
    
    

def main():
    
    

    Border ="-"*50
    print(Border)
    print("-------Marvellous Data Sheild System-----")
    print(Border)

    if(len(sys.argv) ==2):
        if(sys.argv[1] =="--h"or sys.argv[1] =="--H"):
            print("This script is used to :")
            print("1: Takes auto backup at given time")
            print("2: Backup only new and updated files")
            print("3:create an archive of the backup periodically")
            
        elif(sys.argv[1] =="--u"or sys.argv[1] =="--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SoureDirectory : Name of Directory to backed up")
           

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    # python Demo.py 5 Data
    elif(len(sys.argv) ==3):
        print("Inside Project logics")
        print("Time Interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])
        print("Press cntrl + c to stop the ecxection")
        
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataSheildStart,sys.argv[2])
    
    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)

if __name__=="__main__":
    main()