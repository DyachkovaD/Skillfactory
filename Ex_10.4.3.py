import os

def dir_inf(path=os.getcwd()):
     for i in os.walk(path):
         print(i)

dir_inf('D:\data')