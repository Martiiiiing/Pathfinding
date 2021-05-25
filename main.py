import numpy as np
from numpy.core.defchararray import chararray
from allfunctions import *


loop=1
while loop:
    fichier = input("Please type the name of the file:")
    nbnodes, nbedges, edges = readfromtxt(fichier)
    AdjMat = CreateAdjMat(nbnodes,nbedges,edges)
    print("AdjMat is:")
    printMat(AdjMat,nbnodes)
    # print("AdjMat is:")
    # print (AdjMat)

    L,P = FloydWarshall(AdjMat,nbnodes)
    # print(L)
    FindCircuitsAbso(L, nbnodes)
    loop=int(input("Do you want to continue(0/1):"))