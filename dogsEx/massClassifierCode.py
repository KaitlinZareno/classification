from __future__ import print_function
import subprocess
#import path
import os
import glob
import sys


f = open('classList.txt', 'w')  

path = '/home/kzareno/classification/dogsEx/*.jpg'  
count =0

x1 =  './label_image.py' 
x2 = '--graph=./output_graph.pb'
x3 = '--labels=./output_labels.txt'
x4 = '--input_layer=Placeholder'
x5 = '--output_layer=final_result'

files=glob.glob(path)   
for file in files:   
    name  = os.path.basename(file)  
    f.write(name +"\n")
    x6 = '--image=./'+ name 
    args1 = ['echo', '\n', name]
    argument = ['python', x1, x2, x3, x4, x5,x6]
    subprocess.call(args1, stdout=f)
    subprocess.call(argument, stdout=f)

    count +=1 

args3 = ['tail', '-n +'+str(count), 'classList.txt']
#subprocess.call(args3)

#currently prints file names at the end of the classification	
    
