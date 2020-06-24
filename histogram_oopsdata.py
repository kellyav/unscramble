# Data 200
# Mixed up Literature Assignment
# October 24th, 2019 
# File: oops_12.txt
# Alexa Kelly 



import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from collections import defaultdict

#open and read the file:
file=open("oops_12.txt", "r", errors='ignore')
charcount= {}                  #dictionary hold counts
validchars= "abcdefghijklmnopqrstuvwxyzàâæçèéêëîïôùûüœ"   #includes other special letters in the doc 

#frequency table:
print(f'{":":<2}{"Letter":^2}{":":<4}{"Frequency":<5}{":":<2}')

for i in range(97,123):     #range for lowercase characters 
    c=(chr(i))              #characters we included a-z and otherwsie 
    charcount[c]=0          # begin counting at 0
    
current_text= file.read().lower()
for i in range(0,len(validchars)):
    charcount[validchars[i]]= current_text.count(validchars[i])
    
for k,v in charcount.items():
    print(f'{":":<2} {k:^6} {":":<4}{v:<6} {":":>2}')


#histogram:        
num= charcount
x= list(num.values())
y= list(num.keys())

x_coordinates= np.arange(len(num.keys()))        
plt.bar(x_coordinates,x)
plt.xticks(x_coordinates,y)   
plt.title('Occurences of each Letter in Oops_12')
plt.xlabel('Letters')
plt.ylabel('Count')
plt.show()

