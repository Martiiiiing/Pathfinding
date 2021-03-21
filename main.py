import numpy as np

def readfromtxt(fichier):
    file_object = open(fichier,'r')
    nbnodes=int(file_object.readline())
    nbedges=int(file_object.readline())
    edges=np.empty([nbedges,3], dtype=int)

    for i in range (nbedges): 
        temp=file_object.readline()
        temp=temp.split()

        for j in range (3):
            edges[i,j]=int(temp[j])

    # print(edges)    
    return nbnodes, nbedges, edges
 
def CreateAdjMat(nbnodes,nbedges,edges):
    AdjMat=np.empty([nbnodes,nbnodes], dtype=int)
    AdjMat[:]=9999
    for a in range(nbnodes):
        AdjMat[a,a]=0
    # print(AdjMat)
    for i in range (nbedges):
        AdjMat[edges[i,0],edges[i,1]]=edges[i,2]
    print(AdjMat)
    return AdjMat

# def FloydWarshall(AdjMat):
    
fichier=input("Please type the name of the file:")
nbnodes, nbedges, edges = readfromtxt(fichier)
AdjMat=CreateAdjMat(nbnodes,nbedges,edges)