import string
import numpy as np
oops_12 = open('oops_12.txt').read()
oops_12 = oops_12.lower()   # this line makes sure the code is not case senstitive when counting 

# Filter all characters that are not letters.
text = filter(lambda x: x in string.letters, oops_12.lower())
oops_12 = filter(str.isalnum, oops_12)    # this line removes all the characters 

from collections import Counter
c = Counter(oops_12)
print(c, "\n")     # outputs the raw data from the txt file, aka how many letters and their occurances 

C=sorted(c.items())  ## sorts the list from counter (number of letters) into a sorted list
#print(C)   # C outputs a sorted matrix version of c

# turns the list of lists into an array to convert it better 
Frequency_array= np.array(C)
#type(Frequency_array)   #this is a 1d array 
print(Frequency_array)


sortedfreq= Frequency_array[Frequency_array[:,1].argsort()]
print("\n",sortedfreq)