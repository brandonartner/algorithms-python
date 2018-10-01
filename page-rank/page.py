from pprint import pprint
from collections import namedtuple
import copy
from fractions import Fraction
import sys

convergeApprox = 0.00001

def cmpFracList(list1, list2):
	for i in range(0,len(list1)):
		if abs(float(list1[i].numerator)/list1[i].denominator - float(list2[i].numerator)/list2[i].denominator) >= convergeApprox:
			return 0
	return 1

if len(sys.argv) < 2:
	sys.exit("Format: page.py [Input Filename]")

with open(sys.argv[1]) as f:
   Matrix = f.read().splitlines()
length = len(Matrix)
pprint(Matrix)
print(length)
PR = [Fraction(1, length) for _ in range(length)]
Count = [Fraction(0,1) for _ in range(length)]
list1 = []
d = Fraction(3,20)

for q in range(length):
   for s in range(length):
      if Matrix[q][s] is '1':
         Count[q] = Count[q] + Fraction(1,1)
         t=(q,s)
         list1.append(t)

converged = 0
countSteps=1;
while converged == 0:
	print("Step #{}\n".format(countSteps))
	tempPR =  [Fraction(0,1) for _ in range(length)]
	for edge in list1:
		temp = copy.deepcopy(PR[edge[0]])
		tempPR[edge[1]] = tempPR[edge[1]] + temp/Count[edge[0]]

	for x in tempPR:
		x = (Fraction(1,1)-d) +d*x
	if cmpFracList(tempPR,PR) == 1:
		converged = 1

	PR = copy.deepcopy(tempPR)
	pprint(PR)
	countSteps = countSteps + 1

f.close()
