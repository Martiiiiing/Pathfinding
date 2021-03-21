import numpy as np
import math

def readfromtxt(fichier):
    file_object = open(fichier,'r')
    nbnodes = int(file_object.readline())
    nbedges = int(file_object.readline())
    edges = np.empty([nbedges,3], dtype=int)

    for i in range (nbedges): 
        temp = file_object.readline()
        temp = temp.split()

        for j in range (3):
            edges[i,j] = int(temp[j])

    # print(edges)    
    return nbnodes, nbedges, edges
 
def CreateAdjMat(nbnodes,nbedges,edges):
    AdjMat = np.empty([nbnodes,nbnodes], dtype=float)
    AdjMat[:] = np.inf
    for a in range(nbnodes):
        AdjMat[a,a] = 0
    # print(AdjMat)
    for i in range (nbedges):
        AdjMat[edges[i,0],edges[i,1]] = edges[i,2]
    
    return AdjMat

def FloydWarshall(AdjMat,nbnodes):
    L = AdjMat
    P = np.empty([nbnodes,nbnodes], dtype= float)
    for a in range (nbnodes):
        for b in range (nbnodes):
            if AdjMat[a,b] == np.inf:
                P[a,b]=None
            else:
                P[a,b]=a

    for k in range (nbnodes):
        for i in range (nbnodes):
            for j in range (nbnodes):
                if L[i,k] == np.inf or L[k,j]== np.inf:
                    #to prevent overflows
                    temp = np.inf
                else:
                    temp = L[i,k]+L[k,j]
                if L[i,j] > temp:
                    L[i,j] = temp
                    P[i,j] = k
    return L,P

def FindCircuitsAbso(L, nbnodes):
    for i in range (nbnodes):
        if L[i,i]<0:
            print("An absorbant circuit was found")
            return 1

    return 0

fichier = input("Please type the name of the file:")
nbnodes, nbedges, edges = readfromtxt(fichier)
AdjMat = CreateAdjMat(nbnodes,nbedges,edges)
# print(AdjMat)
L,P = FloydWarshall(AdjMat,nbnodes)
print("L matrix is:")
print(L)
print("P Matrix is:")
print(P)
