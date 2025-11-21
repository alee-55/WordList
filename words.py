def num_letters(n_col, n_row):
    return n_col + n_col + n_row + n_row -4

    
import numpy as np
data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')

words = [] 
rows, columns = data.shape  
c1=0
while c1 < columns:
    words.append(str(data[0,c1]))
    c1= c1+1
c2=0
while c2 < columns:
    words.append(str(data[5,c2]))
    c2= c2+1
r1=1
while r1 < rows-1:
    words.append(str(data[r1,0]))
    r1= r1+1
r2=1
while r2 < rows-1:
    words.append(str(data[r2,6]))
    r2= r2+1       
...
print(words) #check that you collected all the letters in your data file

assert len(words) == num_letters(rows, columns) 

  #this should not throw an error. If it does, most likely your main code is not getting the correct number of letters
