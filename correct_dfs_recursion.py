from functions import getNextState
import time
import sys
myVisitedList=[]
def CorrectdfsRecursion(current):
 start_time=time.time()
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
  end_time=time.time()
  print("DFS RECURSION:\n")
  print("path length:", len(path),"\nspace:",sys.getsizeof(myVisitedList)," bytes")
  print(f"\ntime:,{end_time-start_time} seconds") 
 
  return
 nextStates=getNextState(current)
 for next in nextStates:
   next.parent=current
   if next is not None:
     CorrectdfsRecursion(next)