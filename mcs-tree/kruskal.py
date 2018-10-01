import pprint
import re
import sys
import math

def has_edge(edges,start,end):
    contains_edge = 0

    for edge in edges:
        if edge[0] == start and edge[1] == end:
            contains_edge = 1
            break

    return contains_edge

def display(T, n):
    for i in range(n):
        if i > 0:
            for j in range(n):
                if j > 0:
                    sys.stdout.write('   ')
                if has_edge(T,n*(i-1)+j+1, n*i+j+1):
                    sys.stdout.write(' | ')
                else:
                    sys.stdout.write('   ')
            print()
        for j in range(n):
            if j > 0:
                if has_edge(T,n*i+j,n*i+j+1):
                    sys.stdout.write(' - ')
                else:
                    sys.stdout.write('   ')
            sys.stdout.write(' * ')
        print()

filename = input("Select your item: ")

with open(filename) as inputFile:
    #reading in the graph.txt file that will split the first character to see how many nodes the graph will have
    listGraph2 = [tuple(re.split(':',inputFile.readline()))]

#passing in the rest of the list (1,2;9)..etc
s= listGraph2[0][1]
#s=s[1:-1]
pattern = '([0-9]+),'
sub = r'\1;'
Graph = re.sub(pattern,sub,s)
Graph = Graph.split(',')
edges=[]
for i in range(len(Graph)):
    edges.append(eval(Graph[i].replace(';',',')))


for i in range(len(edges)):
    for j in range(i+1, len(edges)):
        if edges[i][2] > edges[j][2]:
            edges[i],edges[j] = edges[j],edges[i]

#just getting num of nodes which is n^2 n indicating the # of nodes
n = int(listGraph2[0][0])
numOfNodes = n**2
for x in edges:
    if x[0] > numOfNodes or x[1] > numOfNodes or abs(math.floor((x[1]-1)/n)-math.floor((x[0]-1)/n)) > 1  or abs((x[1]-1)%n-(x[0]-1)%n) > 1:
        print ("Error not a Graph")
        sys.exit(0)

D = [i for i in range(1,numOfNodes+1)]
T = []
for edge in edges:
    T.append(edge)
    if D[edge[0]-1] == D[edge[1]-1]:
        T.remove(edge)
    else:
        k = D[edge[0]-1]
        l = D[edge[1]-1]
        for j in range(numOfNodes):
            if D[j] == l:
                D[j] = k

print(edges)
display(edges,n)
print(T)
display(T,n)
