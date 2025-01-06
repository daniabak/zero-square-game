import copy
from collections import Counter

def extractMovingCellFromGrid(grid):
        points=[]
        for indexRow, row in enumerate(grid):
            for indexColumn,item in enumerate(row):
                if item=="r":                  
                    points.append((indexRow,indexColumn))                 
                if item=="b":
                    points.append((indexRow,indexColumn))
           
                if item=="y":
                    points.append((indexRow,indexColumn))
             
                if item=="g":
                    points.append((indexRow,indexColumn))
                if item=="p":
                    points.append((indexRow,indexColumn))
        MovingPoints= points+[None] * (5- len(points))      
           
        return MovingPoints
def onpress(levelPatch,update):

    print("press w to move above,\npress s to move down,\npress d to move right,\npress a to move left\npress q to exit\n\n")
    while True: 
      select=input()
      if select=="w":
          update=  levelPatch.moveAbove()
          levelPatchToEqual=copy.deepcopy(levelPatch)
          levelPatch=update
          levelPatch.print_patch()
          if levelPatch.checkWin()==True:         
            print("graduation 🚀🚀🚀")
            break
      if select=="s":
          update=  levelPatch.moveDown()
          levelPatchToEqual=copy.deepcopy(levelPatch)
          levelPatch=update
          levelPatch.print_patch()
          if levelPatch.checkWin()==True:
            
            print("graduation 🚀🚀🚀")
            break 

      if select=="d":  

          update=  levelPatch.moveRight()
          levelPatchToEqual=copy.deepcopy(levelPatch)
          levelPatch=update
          levelPatch.print_patch()
          if levelPatch.checkWin()==True:
            
            print("graduation 🚀🚀🚀")
            break



      if select=="a":

          update=  levelPatch.moveLeft()
          levelPatchToEqual=copy.deepcopy(levelPatch)
          levelPatch=update
          levelPatch.print_patch()
          if levelPatch.checkWin()==True:
            
            print("graduation 🚀🚀🚀")
            break
      if select=="=":
         checkEqualTwoStates(levelPatchToEqual,update)
      elif select=="q":
       break
def getNextState(levelPatch):
 listOfNextState=[]
 points =extractMovingCellFromGrid(levelPatch.grid)
    
 if True in levelPatch.checkMoveableRight(points):
     updated =levelPatch.moveRight()
     listOfNextState.append(updated)

 if True in levelPatch.checkMoveableLeft(points):
     updated =levelPatch.moveLeft()
     listOfNextState.append(updated)

 if True in levelPatch.checkMoveableAbove(points):
   updated =levelPatch.moveAbove()
   listOfNextState.append(updated)
   
 if True in levelPatch.checkMoveableDown(points):
     updated =levelPatch.moveDown()
     listOfNextState.append(updated)
 return listOfNextState  
def checkEqualTwoStates(levelPatch,updatedPatch):
 if levelPatch.grid == updatedPatch.grid :
     print("two state is equal")
 else:
      print("two state is not equal")  

def hurestic(levelPatch):
    dist = 0
    points = extractMovingCellFromGrid(levelPatch.grid)
    pointsWithoutNone = [point for point in points if point is not None]
    goals = levelPatch.goalValues

    visitedStates = set() 
    for movingCell in pointsWithoutNone:
        for goal in goals:
            xT, yT = goal
            xM, yM = movingCell
            if (xM, yM) in visitedStates: 
                dist += 1000  
            else:
                visitedStates.add((xM, yM))
                if str(levelPatch.grid[xM][yM]).upper() == levelPatch.grid[xT][yT]:
                    dist += abs(xM - xT) + abs(yM - yT)
    
    return dist
def duplicateGoalInWhiteGoal(goalValues):
    counts=Counter(goal for goal in goalValues)
    return (True  for count in counts if count>1)
def getAnotherGoals(newPatch,x,y):
 
    Goals=["R","B","Y","G","P"]
    PassingCells= list(set(Goals)-set([str(newPatch.grid[x][y]).upper()]))
    firstPassingCell=    PassingCells[0]
    secondPassingCell=    PassingCells[1]
    thirdPassingCell=    PassingCells[2]
    fourthPassingCell=    PassingCells[3]
  
    return firstPassingCell,secondPassingCell,thirdPassingCell,fourthPassingCell