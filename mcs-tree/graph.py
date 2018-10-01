import pprint
import re
with open('graph.txt') as inputFile:
    #reading in the graph.txt file that will split the first character to see how many nodes the graph will have
    listGraph2 = [tuple(re.split(':',inputFile.readline()))]
#checking if we indeed get that first element i.e. got 2: from text file splitting off the :
print listGraph2[0][0]
#passing in the rest of the list (1,2;9)..etc
Graph = list(listGraph2[0][1])
#print Graph
listGraph=[]
test = 0
for x in Graph:
    #reading from the text file here dont want to include these because we
    #just want the numbers saved into a list
    if(x!="(" and x != ")" and x!=";" and x!=","):
        #print x
        #list graph now has all of the items as the following (1,2,9)...etc read in nicely
       listGraph.append(x)
       test=test+1
#just a test to make sure that is indeed the correct output
print listGraph
#splitting the list into 3 parts because before it was one giant list but we need the 3 parts for the (1,2,9) by #itself
GroupList = zip(*[iter(listGraph)]*3)
print GroupList
for i in range(len(GroupList)):
    for j in range(i+1, len(GroupList)):
        #print GroupList[i][0]
        #print GroupList[j][0]
        #here i am sorting the edges from decreasing order to increasing order
        if GroupList[i][0] > GroupList[j][0]:
            GroupList[i],GroupList[j] = GroupList[j],GroupList[i]
print GroupList
print test
#just getting num of nodes which is n^2 n indicating the # of nodes
numOfNodes = int(listGraph2[0][0])**2
#converted tuple of strings to ints easier to compare
GroupList = [map(int, x) for x in GroupList]
print GroupList
#getting first group of group list which is the edge1
Edge1 = [i[0] for i in GroupList]
print Edge1
#second group list edge 2
Edge2 = [i[1] for i in GroupList]
print Edge2
#3 and final group in list the weights
Weights = [i[2] for i in GroupList]
print Weights
#now i make a matrix with the size of the nodes to obtain the "linking from each node"
Matrix = [[0 for x in range(numOfNodes)]for y in range(numOfNodes)]
pprint.pprint(Matrix)
for i in range(len(Edge1)):
       Matrix[Edge1[i]-1][Edge2[i]-1] = 1

#print numOfNodes
numEdges = numOfNodes+1
#print numEdges
pprint.pprint(Matrix)
Connection=[]
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                  for row in Matrix]))
#checking to see if input is a graph
errorCheck=0
for q in range(numOfNodes):
    for s in range(numOfNodes):
        if Matrix[q][s] is 1:
            t=(q+1,s+1)
            Connection.append( t )
#implementation of Kruskal's algorithm empty graph is Matrix2 with the number of Nodes
Matrix2 = [['*' for x in range(len(Connection))]for y in range(len(Connection)/2)]
print Matrix2
print Connection
errorCheck=0
for x, y in zip(Connection, Connection[0:]):
    if y[1] - x[0] > numOfNodes/2 or y[1] - x[0] < 0:
        print "Error not a Graph"
        errorCheck=-1
if errorCheck != -1:
    #sorting the cost of all the edges c(e1)<=c(e2)<=c(e3)<=c(e4)
    for i in range(len(GroupList)):
        for j in range(i+1, len(GroupList)):
            #print GroupList[i][0]
            #print GroupList[j][0]
            #here i am sorting the edges from decreasing order to increasing order
            if GroupList[i][2] > GroupList[j][2]:
                GroupList[i],GroupList[j] = GroupList[j],GroupList[i]


    

    print GroupList