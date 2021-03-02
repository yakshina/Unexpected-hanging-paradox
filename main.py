import random
import numpy as np
import matplotlib.pyplot as plt
num = 10000 
q = 0
o = 0 
x = [] 
y = []
for i in range(num):
    all_prisoners = set ([1 ,2 ,3])
    possible_prisoners1 = all_prisoners.copy()
    possible_prisoners2 = all_prisoners.copy()
    
    free = random . randint (1 ,3) 
    
    a = random.randint(1,3)
    
    possible_prisoners1.remove(free)
    
    if free != a:
        possible_prisoners1.remove(a)
    
    b = possible_prisoners1.pop()
    
    possible_prisoners2.remove(a) 
    possible_prisoners2 .remove(b) 
    c = possible_prisoners2.pop()
        
    if a == free: 
        q +=1
        x.append(q/num)
    if c == free: 
        o +=1
        y.append(o/num)
        
print(q/num)
print(o/num)
plt.plot(x)
