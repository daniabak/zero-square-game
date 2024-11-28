from functions import getNextState
myVisitedList=[]
def CorrectdfsRecursion(current):
 if current == None or current.grid in (state.grid for state in myVisitedList):
        return
 myVisitedList.append(current)
 if current.checkWin():
  path=[]
  while current:
   path.append(current)
   current=current.parent
  path.reverse()
  for i in path:
   i.print_patch()
  print("visited list length ",len(myVisitedList ),)
  print("path length:",len(path))
  print("_________finished dfs recursion_______") 
  return
 nextStates=getNextState(current)
 for next in nextStates:
   next.parent=current
   if next is not None:
     CorrectdfsRecursion(next)