from levels import levelsPatch 
from patch import  Patch
from functions import onpress
from bfs import bfsSolving 
from dfs import dfsSolving 

import copy 
def selectedPlayer():
    player = input("select type of player:\n1-normal player\n2-Bfs player\n3-Dfs player\n\n")
    if player == "1":
     patch = levelsPatch(int(input("select levels : 1 2 3 4 5 6\n")))        
     levelPatch=copy.deepcopy(patch)
     levelPatch.print_patch()
     update=Patch
     onpress(levelPatch,update)
    elif player == "2":
     patch = levelsPatch(int(input("select levels : 1 2 3 4 5 6\n")))        
     levelPatch=copy.deepcopy(patch)
     levelPatch.print_patch()
    #  update=Patch
     bfsSolving(levelPatch)
    elif player == "3":
     patch = levelsPatch(int(input("select levels : 1 2 3 4 5 6\n")))        
     levelPatch=copy.deepcopy(patch)
     levelPatch.print_patch()
    #  update=Patch
     dfsSolving(levelPatch)
      
    else:
      print("wrong input")