import copy

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
        MovingPoints= points+[None] * (4- len(points))      
           
        return MovingPoints
def onpress(levelPatch,update):

    while True: 
      select=input("press w to move above,\npress s to move down,\npress d to move right,\npress a to move left\npress q to exit\n\n")
      if select=="w":
        update,win=  levelPatch.moveAbove()
        levelPatchToEqual=copy.deepcopy(levelPatch)
        levelPatch=update
        if win ==True:
         break
        levelPatch.print_patch()
       
      if select=="s":
        update,win= levelPatch.moveDown()
        levelPatchToEqual=copy.deepcopy(levelPatch)
        levelPatch=update
        if win ==True:
         break
        levelPatch.print_patch()
      if select=="d":
        update,win= levelPatch.moveRight()
        levelPatchToEqual=copy.deepcopy(levelPatch)
        levelPatch=update
        if win ==True:
         break
        levelPatch.print_patch()

      if select=="a":
        update,win= levelPatch.moveLeft()
        levelPatchToEqual=copy.deepcopy(levelPatch)
        levelPatch=update
        if win ==True:
         break
        levelPatch.print_patch() 
      if select=="e":
        getAllMoves(levelPatch) 
      if select=="=":
         checkEqualTwoStates(levelPatchToEqual,update)
      elif select=="q":
       break
def getAllMoves(levelPatch):
 points =extractMovingCellFromGrid(levelPatch.grid)
 if True in levelPatch.checkMoveableAbove(points):
   updated,_ =levelPatch.moveAbove()
   print("state to move up")
   updated.print_patch() 
 if True in levelPatch.checkMoveableDown(points):
     updated,_ =levelPatch.moveDown()
     print("state to move down")
     updated.print_patch() 
 if True in levelPatch.checkMoveableRight(points):
     updated,_ =levelPatch.moveRight()
     print("state to move right")
     updated.print_patch() 
 if True in levelPatch.checkMoveableLeft(points):
     updated,_ =levelPatch.moveLeft()
     print("state to move left")
     updated.print_patch() 

 print("Basic state") 
 levelPatch.print_patch()
def checkEqualTwoStates(levelPatch,updatedPatch):
 if levelPatch.grid == updatedPatch.grid :
     print("two state is equal")
 else:
      print("two state is not equal")  