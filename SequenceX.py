#Numeric
###################################################################################
#  File Name   :     SequenceX.py
#  Description :     Datatypes in python
#                  
#  Input       :         
#  Output      :        
#  Author      :      Rutuja Bharat varal
#  Date        :      21/12/2025
#
###################################################################################

#supports Duplicate
Value1=[10,20,30,40,10]    #[] for List 
print(Value1[0]) #10
Value1[2]=35
print(Value1[2])

#supports Duplicate
Value2=(10,20,30,40,10)    #()for tuple 
print(Value2[0]) #10
#Value2[2]=35               #TypeError: 'tuple' object does not support item assignment 


# Not supports Duplicate
Value3={10,20,30,40,10}     #{}for set 
#print(Value3[0])           # TypeError: 'set' object is not subscriptable




