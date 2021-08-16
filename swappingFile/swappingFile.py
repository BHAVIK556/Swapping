# def swapFileData():
file1=input("enter file sorce")
file2=input("enter file sorce")
with open(file1,"r")as a:
 data_a=a.read()

with open(file2,"r")as b:
 data_b=b.read()
    

with open(file1,"w")as a:
 data_a=a.write()
    
 with open(file2,"w")as b:
  data_b=b.write()
  
    # swapFileData()