import os

import numpy as np

T =np.array([],dtype=np.double)
P =np.array([],dtype=np.double)
E =np.array([],dtype=np.double)
p2 =np.array([],dtype=np.double)

with open("stats_var.txt","r") as f:
    while True:
        a = f.readline()
        a=a.split()
        print(a)
        if a == []:
            break
        T = np.append(T,a[0])
        P = np.append(P,a[1])
        E = np.append(E,a[2])
        p2 = np.append(p2,a[3])
print("temperture is :",T)
print("\n")

print("P is :",P,"\n")
print("E is :",E,"\n")
print("P2 is :",p2,"\n")        
