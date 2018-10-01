import pprint
import re
with open('graph.txt') as inputFile:
    #reading in the graph.txt file that will split the first character to see how many nodes the graph will have
    listGraph2 = [tuple(re.split(':',inputFile.readline()))]
#checking if we indeed get that first element i.e. got 2: fom text file splitting off the :
#print listGraph2[0][0]
#passing in the rest of the list (1,2;9)..etc
Graph = list(re.split('),(', listGraph2[0][1]))
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
#print GroupListz
for i in range(len(GroupList)):
    for j in range(i+1, len(GroupList)):
        #here i am sorting the edges from decreasing order to increasing order
        if GroupList[i][0] > GroupList[j][0]:
            GroupList[i],GroupList[j] = GroupList[j],GroupList[i]

#just getting num of nodes which is n^2 n indicating the # of nodes
numOfNodes = int(listGraph2[0][0])**2
#converted tuple of strings to ints easier to compare
GroupList = [map(int, x) for x in GroupList]

#getting first group of group list which is the edge1
Edge1 = [list(i)[0] for i in GroupList]
#print Edge1
#second group list edge 2
Edge2 = [list(i)[1] for i in GroupList]

#3 and final group in list the weights
Weights = [i[2] for i in GroupList]

#now i make a matrix with the size of the nodes to obtain the "linking from each node"
Matrix = [[0 for x in range(numOfNodes)]for y in range(numOfNodes)]

for i in range(len(Edge1)):
       Matrix[Edge1[i]-1][Edge2[i]-1] = 1


numEdges = numOfNodes+1

Connection=[]

#checking to see if input is a graph
errorCheck=0
for q in range(numOfNodes):
    for s in range(numOfNodes):
        if Matrix[q][s] is 1:
            t=(q+1,s+1)
            Connection.append( t )
#implementation of Kruskal's algorithm empty graph is Matrix2 with the number of Nodes
Matrix2 = [['*' for x in range((len(Connection)/2))] for y in range((len(Connection)/2))]

errorCheck=0
for x, y in zip(Connection, Connection[0:]):
    if y[1] - x[0] > numOfNodes/2 and [ y[1] - x[0] < 0 and y[1]-x[0] != -1 or y[1]-x[0] != -2]:
        print( y[1]-x[0])
        print ("Error not a Graph")
        errorCheck=-1
if errorCheck != -1:
    #sorting the cost of all the edges c(e1)<=c(e2)<=c(e3)<=c(e4)
    for i in range(len(GroupList)):
        for j in range(i+1, len(GroupList)):
            #here i am sorting the edges from decreasing order to increasing order
            if GroupList[i][2] > GroupList[j][2]:
                GroupList[i],GroupList[j] = GroupList[j],GroupList[i]
check = 1
count = 2
newList=[]
nextList=[]
for  x, y in zip(GroupList, GroupList[0:]):
    check = check +1
    if y[1]-x[0] == -1 or y[1]-x[0] == 1 and check < numEdges:
        GroupList.insert(count,'-')
        newList.append('-')
        nextList.append((x[0],y[1]))
        count = count -1
    if y[1]-x[0] == -2 or y[1]-x[0] == 2 and check < numEdges:
        GroupList.insert(count,'|')
        newList.append('|')
        nextList.append((x[0],y[1]))
        count = count-1
newList.append('')
for i in range(len(newList) - 1):
  print ('*  ' ,)
  if i == (numOfNodes/2) - 1:
    print
    for j in range(len(newList)):
        if newList[j] == '|':
            print (newList[j] + "  ",)
        if newList[j] == '-':
            hey = newList[j] + "",
    print
print ("\b\b" + hey[0],)
print ('*')
