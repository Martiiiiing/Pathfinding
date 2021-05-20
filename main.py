import numpy as np
import math

from numpy.core.defchararray import chararray

def readfromtxt(fichier):
    file_object = open(fichier,'r')
    nbnodes = int(file_object.readline())
    nbedges = int(file_object.readline())
    edges = np.empty([nbedges,3], dtype=int)

    for i in range (nbedges): 
        temp = file_object.readline() #reads each line
        temp = temp.split()# splits each string using " " as separator

        for j in range (3):
            edges[i,j] = int(temp[j]) #converts strings to int and puts it into the table

    # print(edges)    
    return nbnodes, nbedges, edges
 
def CreateAdjMat(nbnodes,nbedges,edges):
    AdjMat = np.empty([nbnodes,nbnodes], dtype=float) #init numpy array
    AdjMat[:] = np.inf #sets all values to inf
    for a in range(nbnodes):
        AdjMat[a,a] = 0 #sets the distance between each to itself as 0
    # print(AdjMat)
    for i in range (nbedges):
        AdjMat[edges[i,0],edges[i,1]] = edges[i,2] #fills the rest of the adj matrix 
    
    return AdjMat


def printMat(mat, nbnodes):
    mat2=np.empty([nbnodes+1,nbnodes+1],dtype=chararray)
    mat2[0,0]=" "
    for i in range (nbnodes):
        mat2[0,i+1]="col "+str(i)
        mat2[i+1,0]=str(i)
        for j in range(nbnodes):
            mat2[i+1,j+1]=str(mat[i,j])
            if len(mat2[i+1,j+1]) >=6:
                mat2[i+1,j+1]=None
            while len(mat2[i+1,j+1]) <5:
                mat2[i+1,j+1]=mat2[i+1,j+1]+" "
            
    print(mat2)

def FloydWarshall(AdjMat,nbnodes):
    L = AdjMat
    P = np.empty([nbnodes,nbnodes], dtype= float)
    for a in range (nbnodes):
        print("L matrix at iteration "+ str(a) + " is:")
        printMat(L,nbnodes)
        print("P matrix at iteration "+ str(a) + " is:")
        printMat(P,nbnodes)
        for b in range (nbnodes):
            if AdjMat[a,b] == np.inf:
                P[a,b]=None
            else:       #Filling P matrix which is a matrix containing the last predecessor of the walk in question
                P[a,b]=a
            for c in range (nbnodes):
                if L[b,a] == np.inf or L[a,c]== np.inf:
                    
                    temp = np.inf
                else:
                    temp = L[b,a]+L[a,c]
                if L[b,c] > temp:
                    L[b,c] = temp   #if we find a shorter path using and intermediary vertex we replace the weight in L matrix
                    P[b,c] = a  # and update P putting the name of that intermediary
                  
    return L,P

def FindCircuitsAbso(L, nbnodes):
    for i in range (nbnodes): # we check each vertex
        if L[i,i]<0: #There is a cicle if the distance of a vertex to itself < 0 
            print("An absorbant circuit was found")
            return 1

        print("No absorbant circuit was found")
        return 0
    

fichier = input("Please type the name of the file:")
nbnodes, nbedges, edges = readfromtxt(fichier)
AdjMat = CreateAdjMat(nbnodes,nbedges,edges)

# print("AdjMat is:")
# print (AdjMat)

L,P = FloydWarshall(AdjMat,nbnodes)

FindCircuitsAbso(L, nbnodes)