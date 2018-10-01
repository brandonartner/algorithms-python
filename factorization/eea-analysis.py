
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import random
from pprint import pprint
import time
import numpy as np
import matplotlib.pyplot as pyplot


N = 100
Trials = 1000

def EEA(m,n):
    if(m <= 0 or n <= 0):
        return 0,0,0,0
    a = 0; x = 1; b = 1; y = 0; c = m; d = n; loops = 0;
    while(1):
        loops += 1
        q = c/d
        r = c%d
        if(r == 0):
            break
        c = d; d = r; t = x; x = a;
        a = t - q*a;
        t = y; y = b;
        b = t - q*b;
    return a,b,d,loops


data = [[0]*Trials for i in range(N-1)]
averages = [0]*(N-1)
numOfRelPrimes = 0
start = time.time()
for i in range(2,N+1):
    print("Input Length: %d" %i)
    for j in range(1,Trials+1):
        print("\tTrial #%d" %j)
        fullInput = 2**(i+1)-1
        mask = random.randint(1,fullInput)
        #m = random.randint(1,2**(i+1)-1)
        m = fullInput & mask
        n = fullInput & (~mask)
        #n = ~m
        a,b,d,loops = EEA(abs(m),abs(n))
        data[i-2][j-1] = loops
        print "\t\t%d*%d + %d*%d = %d = gcd(%d,%d) ----------- # of Loops: %d \n" %(a,m,b,n,d,m,n,loops)
    sum = 0
    for j in range(1,Trials+1):
        sum += data[i-2][j-1]
    averages[i-2] = sum/Trials
stop = time.time()
length = int(stop) - int(start)
pyplot.plot(averages)
pyplot.ylim([0,max(averages)])
pyplot.xlim([0,N])
pyplot.xlabel('Input Size added together', fontsize=18)
pyplot.ylabel('Average # of steps', fontsize=16)
pyplot.show()
pprint(averages)
pprint(max(averages))
print("Time Elapsed: %d" %length)