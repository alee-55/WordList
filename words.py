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
print(words) 

assert len(words) == num_letters(rows, columns)

### Part 4

words2 = [] 
rows, columns = data.shape  
c1=0
while c1 < columns-1:
    words2.append(str(data[0,c1])+str(data[0,c1+1]))
    c1= c1+1
c2=0
while c2 < columns-1:
    words2.append(str(data[5,c2])+str(data[5,c2+1]))
    c2= c2+1
r1=1
while r1 < rows-2:
    words2.append(str(data[r1,0])+str(data[r1+1,0]))
    r1= r1+1
r2=1
while r2 < rows-2:
    words2.append(str(data[r2,6])+str(data[r2+1,6]))
    r2= r2+1       
...
print(words2) 

assert len(words2) == num_letters(rows, columns)-4

