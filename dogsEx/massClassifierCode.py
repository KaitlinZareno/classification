from __future__ import print_function
import subprocess
#import path
import os
import glob
import sys


f = open('classList.txt', 'w')  

#path = '/home/kzareno/Desktop/sandbox/research/RatVideos/*.jpg'
path = '/home/kzareno/example_code/dogsEx/*.jpg'  
count =0
#chmod +x label_image.py
x1 =  'label_image.py' 
x2 = '--graph=./retrained1_graph.pb'
x3 = '--labels=./retrained1_labels.txt'
x4 = '--input_layer=Placeholder'
x5 = '--output_layer=final_result'
x7 = '>classList.txt'
#x7 = '| tee classList.txt;'

files=glob.glob(path)   
for file in files:   
    name  = os.path.basename(file)  
    f.write(name +"\n")
    x6 = '--image=./'+ name  
    argument = ['python', x1, x2, x3, x4, x5,x6]
    subprocess.call(argument)
    #args2 = [x7]
    #subprocess.call(args2)
    sys.stdout = f
    f.write("\n\n")
    #print (filename)
    count +=1 

#f.close()
    
