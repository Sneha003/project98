import os
import shutil
def data():

    file1=input("enter source folder name: ")
    file2= input("enter destination folder name: ")

    with open(file1,"r") as a:
        data1=a.read()
        
    with open(file2,"r") as b:
        data2=b.read()    

    with open (file1,"w")  as a:
        a.write(data2) 
    with open (file2,"w") as b:
        b.write(data1)
        
data()

