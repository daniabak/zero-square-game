from levels import levelsPatch 
from patch import  Patch
from functions import onpress
from bfs import bfsSolving 
from dfs import dfsSolving 
from correct_dfs_recursion import CorrectdfsRecursion
from ucs import ucs_solving
from a_star import aStar
from hillClimb import hillClimbing
from steapest_hill_climbing import steapestHillClimbing
import copy 
def selectedPlayer():
    player = input("select type of player:\n1-normal player\n2-Bfs player\n3-Dfs player\n4-Dfs recursion\n5-Ucs player\n6-a star\n7-simple hill climbing\n8-steepest hill climbing\n")
    if player == "1":
     patch = levelsPatch(int(input("select levels : 1 2 3 4 5 \n for levels of zero game : 10 20 30\n")))        
     levelPatch=copy.deepcopy(patch)
     levelPatch.print_patch()
     update=Patch
     onpress(levelPatch,update)
    elif player == "2":
     patch = levelsPatch(int(input("select levels : 1 2 3 4 5 \n for levels of zero game : 10 20 30\n")))        
     levelPatch=copy.deepcopy(patch)
     bfsSolving(levelPatch)

    elif player == "3":
     patch = levelsPatch(int(input("select levels : 1 2 3 4 5 \n for levels of zero game : 10 20 30\n")))        
     levelPatch=copy.deepcopy(patch)
     dfsSolving(levelPatch)

    elif player == "4":
     patch = levelsPatch(int(input("select levels : 1 2 3 4 5 \n for levels of zero game : 10 20 30\n")))        
     levelPatch=copy.deepcopy(patch)
     CorrectdfsRecursion(levelPatch,)

    elif player == "5":
     patch = levelsPatch(int(input("select levels : 1 2 3 4 5 \n for levels of zero game : 10 20 30\n")))        
     levelPatch=copy.deepcopy(patch)
     ucs_solving(levelPatch)
    elif player == "6":
     patch = levelsPatch(int(input("select levels : 1 2 3 4 5 \n for levels of zero game : 10 20 30\n")))        
     levelPatch=copy.deepcopy(patch)
     aStar(levelPatch)
    elif player == "7":
     patch = levelsPatch(int(input("select levels : 1 2 3 4 5 \n for levels of zero game : 10 20 30\n")))        
     levelPatch=copy.deepcopy(patch)
     hillClimbing(levelPatch)
    elif player == "8":
     patch = levelsPatch(int(input("select levels : 1 2 3 4 5 \n for levels of zero game : 10 20 30\n")))        
     levelPatch=copy.deepcopy(patch)
     steapestHillClimbing(levelPatch)
      
    else:
      print("wrong input")