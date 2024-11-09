from levels import levelsPatch 
from patch import  Patch
from functions import onpress
   
import copy 
def selectedPlayer():
    player = input("select type of player:\n1-normal player\n\n")
    if player == "1":
     patch = levelsPatch(int(input("select levels : 1 2 3 4 5 6\n")))        
     levelPatch=copy.deepcopy(patch)
     levelPatch.print_patch()
     update=Patch
     onpress(levelPatch,update)
      
    else:
      print("wrong input")