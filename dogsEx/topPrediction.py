from __future__ import print_function
import subprocess
#import path
import os
import glob
import sys


f1 = open('placement.txt', 'w')  
f2 = open('topClass.txt', 'w') 

path = '/home/kzareno/classification/dogsEx/'  
count =0

x1 =  "awk"
x2 = "(NR-1)%7<3"
x3 = "classList.txt"

argument = [x1, x2,x3]
subprocess.call(argument, stdout = f1)

with open("placement.txt") as f:
    contents = f.read()
    count = contents.count(".jpg")
    count = ((count/2)/2)+1

x8= "head" 
x9="-n"
x10= "-"+ str(count)
x11= "placement.txt"

args3 = [x8,x9,x10,x11]
subprocess.call(args3, stdout = f2)



#currently prints file names at the end of the classification	
    
