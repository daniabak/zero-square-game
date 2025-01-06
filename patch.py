import copy

from functions import extractMovingCellFromGrid ,duplicateGoalInWhiteGoal,getAnotherGoals
directionLogs=[]
class Patch:

    def __init__(self, n,m):
        # m to column number
        #n to row number
        self.grid = [["." for _ in range(m)] for _ in range(n)]
        self.parent =None
        self.cost=0
        self.goalValues={}
       

    def __lt__(self, other):
        return self.cost < other.cost
    def set_wall(self, x, y):
        self.grid[x][y] = "#"

    def set_goal(self, x, y,color):
        self.grid[x][y] = color
        self.goalValues[(x,y)]=color
    def set_white_goal(self, x, y):
        self.grid[x][y] = "?"
        self.goalValues[(x,y)]="?"
    def set_slim_wall(self, x, y):
        self.grid[x][y] = "@"

    def set_moving_cell(self, x, y,color):
        self.grid[x][y] = color

    def print_patch(self):
       
        for row in self.grid:
            print("   ".join(cell for cell in row))
        print()

            
       

    def checkMoveableAbove(self,points):
     resultCheck = []
     points.sort(key=lambda x: (x is None, x) )
    
     for point in points:
        if point is not None:
            x, y = point
            firstPassingCell,secondPassingCell,thirdPassingCell,fourthPassingCell=getAnotherGoals(self,x,y)
            if x > 0 and self.grid[x - 1][y] == "."or self.grid[x-1][y]==firstPassingCell or self.grid[x-1][y]==secondPassingCell or self.grid[x-1][y]== thirdPassingCell or self.grid[x-1][y]==fourthPassingCell or self.grid[x-1][y] =="?" or self.grid[x-1][y] =="@" or self.grid[x-1][y]==str(self.grid[x][y]).upper() :
                resultCheck.append(True)
            else:
                resultCheck.append(False)
     return resultCheck
    
    def moveAbove(self):
       newPatch = copy.deepcopy(self) 
       points=extractMovingCellFromGrid(newPatch.grid)
       checkList  =  newPatch.checkMoveableAbove(points)
       points.sort(key=lambda x: (x is None, x) )
       resultList=dict( zip(points,checkList))
       for point, canMove in resultList.items():       
            if canMove:
                x, y = point 
                initCell = newPatch.grid[x][y]
                firstPassingCell,secondPassingCell,thirdPassingCell,fourthPassingCell=getAnotherGoals(newPatch,x,y)
                if (x, y) in newPatch.goalValues:
                  newPatch.grid[x][y] = newPatch.goalValues[(x, y)]
                else:
                  newPatch.grid[x][y] = "."
                while x > 0 and newPatch.grid[x - 1][y] == "." or newPatch.grid[x - 1][y]==firstPassingCell or newPatch.grid[x - 1][y]==secondPassingCell or newPatch.grid[x - 1][y]==thirdPassingCell or newPatch.grid[x - 1][y]==fourthPassingCell  :
                    x -= 1
                    self.cost+=1
                if x>0 and newPatch.grid[x-1][y]=="?":
                        x=x-1
                        newPatch.set_goal(x,y,str(initCell).upper())
                        if duplicateGoalInWhiteGoal(newPatch.goalValues):
                            self.cost+=1e11
                if  x>0 and newPatch.grid[x-1][y]=="@":
                         self.cost+=1e11            
                if x>0 and newPatch.grid[x-1][y]==str(initCell).upper():
                         del newPatch.goalValues[(x-1,y)]
                         newPatch.grid[x - 1][y] = "."
                         initCell="."
                newPatch.grid[x][y] = initCell
    #    print("self.cost in above",self.cost)
       directionLogs.append("up")

       return newPatch
    def checkWin(self):
       if len(self.goalValues)==0:
       
           return True
       else:
           return False

    def moveDown(self):

       newPatch=copy.deepcopy(self)
       points=extractMovingCellFromGrid(newPatch.grid)
       checkList  =  self.checkMoveableDown(points)
       points.sort(key= lambda x:(x is None ,x),reverse=True)
       resultList=dict( zip(points,checkList))    
       for point,canMove in resultList.items():
          if canMove: 
            x,y=point
            initCell= newPatch.grid[x][y]
            firstPassingCell,secondPassingCell,thirdPassingCell,fourthPassingCell=getAnotherGoals(newPatch,x,y)
            if (x, y) in newPatch.goalValues:
                    newPatch.grid[x][y] = newPatch.goalValues[(x, y)]
            else:
                    newPatch.grid[x][y] = "."
            while newPatch.grid[x+1][y] =="." or newPatch.grid[x + 1][y]==firstPassingCell or newPatch.grid[x + 1][y]==secondPassingCell or newPatch.grid[x + 1][y]==thirdPassingCell or newPatch.grid[x + 1][y]==fourthPassingCell:               
               x+=1 
               self.cost+=1
            if x < len(self.grid)-1 and  newPatch.grid[x+1][y]=="?":
                        x=x+1
                        newPatch.set_goal(x,y,str(initCell).upper())
                        if duplicateGoalInWhiteGoal(newPatch.goalValues):
                            self.cost+=1e11
            if x < len(self.grid)-1 and  newPatch.grid[x+1][y]=="@":
                         self.cost+=1e11   
            if x < len(self.grid)-1 and newPatch.grid[x+1][y]==str(initCell).upper():
                         del newPatch.goalValues[(x+1,y)]
                         newPatch.grid[x +1][y] = "."
                         initCell="."
                               
            newPatch.set_moving_cell(x,y,initCell)
    #    print("self.cost in down",self.cost)
       directionLogs.append("down")
       return newPatch 

    def moveLeft(self):
       newPatch = copy.deepcopy(self)
       points=extractMovingCellFromGrid(newPatch.grid)
       checkList  =  newPatch.checkMoveableLeft(points)
       points.sort(key=lambda x: (x is None, x[1] if x is not None else None))
       resultList=dict( zip(points,checkList))
       for point,canMove in resultList.items():
              
          if canMove: 
            x,y=point
            initCell= newPatch.grid[x][y]
            firstPassingCell,secondPassingCell,thirdPassingCell,fourthPassingCell=getAnotherGoals(newPatch,x,y)
            if (x, y) in newPatch.goalValues:
                    newPatch.grid[x][y] = newPatch.goalValues[(x, y)]
            else:
                    newPatch.grid[x][y] = "."
            while newPatch.grid[x][y-1] =="."or newPatch.grid[x][y-1]==firstPassingCell or newPatch.grid[x][y-1]==secondPassingCell or newPatch.grid[x][y-1]== thirdPassingCell or newPatch.grid[x][y-1]== fourthPassingCell:              
               y-=1
               self.cost+=1
            if y > 0 and   newPatch.grid[x][y-1]=="?":
                        y=y-1
                        newPatch.set_goal(x,y,str(initCell).upper())
                        if duplicateGoalInWhiteGoal(newPatch.goalValues):
                            self.cost+=1e11
            if y > 0 and   newPatch.grid[x][y-1]=="@":
                         self.cost+=1e11
            if y > 0 and  newPatch.grid[x][y-1]==str(initCell).upper():
                         del newPatch.goalValues[(x,y-1)]
                         newPatch.grid[x ][y-1] = "."
                         
                         initCell="."
          
            newPatch.set_moving_cell(x,y,initCell)
    #    print("self.cost in left",self.cost)
       directionLogs.append("left")
       return newPatch 
       
    def moveRight(self):
       newPatch=copy.deepcopy(self)
       points=extractMovingCellFromGrid(newPatch.grid)
       checkList  =  newPatch.checkMoveableRight(points)
       points.sort(key=lambda x: (x is None, x[1] if x is not None else None),reverse=True)
       resultList=dict( zip(points,checkList))
       for point,canMove in resultList.items():

          if canMove: 
            x,y=point
            initCell= newPatch.grid[x][y]
            firstPassingCell,secondPassingCell,thirdPassingCell,fourthPassingCell=getAnotherGoals(newPatch,x,y)
            if (x, y) in newPatch.goalValues:
                    newPatch.grid[x][y] = newPatch.goalValues[(x, y)]
            else:
                    newPatch.grid[x][y] = "."
            while newPatch.grid[x][y+1] =="."or newPatch.grid[x][y+1]==firstPassingCell or newPatch.grid[x][y+1]==secondPassingCell or newPatch.grid[x][y+1]== thirdPassingCell or newPatch.grid[x][y+1]== fourthPassingCell :              
               y+=1
               self.cost+=1
            if y < len(self.grid[0])-1 and newPatch.grid[x][y+1]=="?":
                        y=y+1
                        newPatch.set_goal(x,y,str(initCell).upper())
                        if duplicateGoalInWhiteGoal(newPatch.goalValues):
                            self.cost+=1e11
            if y < len(self.grid[0])-1 and newPatch.grid[x][y+1]=="@":
                         self.cost+=1e11   
            if newPatch.grid[x][y+1]==str(initCell).upper():
                         del newPatch.goalValues[(x,y+1)]
                         newPatch.grid[x ][y+1] = "."
                         
                         initCell="."
                 
            newPatch.set_moving_cell(x,y,initCell)
    
    #    print("self.cost in right",self.cost)
       directionLogs.append("right")
       return newPatch
    def checkMoveableDown(self,points):
     resultCheck = []
     points.sort(key= lambda x:(x is None ,x),reverse=True)
     for point in points:
        if point is not None:
            x, y = point
            firstPassingCell,secondPassingCell,thirdPassingCell,fourthPassingCell=getAnotherGoals(self,x,y)
            if x < len(self.grid)-1 and self.grid[x + 1][y] == "."or self.grid[x+1][y]==firstPassingCell or self.grid[x+1][y]==secondPassingCell or self.grid[x+1][y]== thirdPassingCell or self.grid[x+1][y]== fourthPassingCell  or self.grid[x+1][y]== "@"  or self.grid[x+1][y]== "?" or self.grid[x+1][y]==str(self.grid[x][y]).upper() :
                resultCheck.append(True)
            else:
                resultCheck.append(False)
        else:
           resultCheck.append(None)        
     return resultCheck

    def checkMoveableLeft(self, points):
     resultCheck = []
     points.sort(key=lambda x: (x is None, x[1] if x is not None else None))
     for point in points:
        if point is not None:
            x, y = point
            firstPassingCell,secondPassingCell,thirdPassingCell,fourthPassingCell=getAnotherGoals(self,x,y) 
            if y > 0 and self.grid[x ][y-1] == "."or self.grid[x][y-1]==firstPassingCell or self.grid[x][y-1]==secondPassingCell or self.grid[x][y-1]== thirdPassingCell or self.grid[x][y-1]== fourthPassingCell  or self.grid[x][y-1]== "@"  or self.grid[x][y-1]== "?" or self.grid[x][y-1]==str(self.grid[x][y]).upper():
                resultCheck.append(True)
            else:
                resultCheck.append(False)
        else:
           resultCheck.append(None)        
     return resultCheck

    def checkMoveableRight(self,points):
     resultCheck = []
     points.sort(key=lambda x: (x is None, x[1] if x is not None else None),reverse=True)
     for point in points:
        if point is not None:
            x, y = point 
            firstPassingCell,secondPassingCell,thirdPassingCell,fourthPassingCell=getAnotherGoals(self,x,y)
            if y < len(self.grid[0])-1 and self.grid[x ][y+ 1] == "."or self.grid[x][y+1]==firstPassingCell or self.grid[x][y+1]==secondPassingCell or self.grid[x][y+1]== thirdPassingCell or self.grid[x][y+1]== fourthPassingCell  or self.grid[x][y+1]== "@"  or self.grid[x][y+1]== "?" or self.grid[x][y+1]==str(self.grid[x][y]).upper():
                resultCheck.append(True)
            else:
                resultCheck.append(False)
        else:
           resultCheck.append(None)
     return resultCheck
