# #count= 3
# #if count>3:
# #    print("Count is greater than 3")
# #elif count ==3:
#  #       print("Count is equal to 3")
# #else:
#  #   print("count less 3")  
#  #another way:
# #message = "greater than 3" if count>3 else "less than 3"
# #print(message)
# #if "zg"> "bpplee":
# # print("bag bigger")
# #print(ord("a"))
# #for x in [1,2,3,4]:
# #    print(x)
# #for x in "dania":
# #    print(x)
# #y=0
# #for x in range(1,10):
#   #  if x%2==0:
#  #       y+=1
# #        print(x)
# #print(f"you have {y} evens") 
# #    
# # def sum(*numbers):
# #   total =0
# #   for x in numbers:
# #     total+=x
    
# #   return total
# # print(sum(1,3,3,3,4,5))
# # mbers=['z','b','d','e','f']
# # numbers=[1,2,3,9,5,6]
# # dd=mbers.sort()
# # print(mbers)
# # for index in enumerate(numbers):
# #     print(index[0],index[1])
# # items=[ 
# #         ("pr1",10),
# #         ("pr2",3),
# #         ("pr3",8) 
# #       ]
# # def sortt(item):
#     # return item[1]
# # items.sort(key=sortt)    
# # print(items)
# # another way lambda 





# # numbers =[1,2,3,4]

# # mapp =[item[1] for item in items if item[1]>4]
# # print(list(mapp))


# # from collections import deque
# # queue = deque([])
# # queue.append(1)
# # queue.append(2)
# # first= [1,2,3,4]
# # sec=[7,8]
# # combi=[*first,*sec,*"hello"]
# # print(combi)  # [1, 2, 3, 4, 7 
# # from pprint import pprint
# # sentence="This is the most common interview question"
# # max =0

# # for x in sentence:
# #  ss= sentence.count(x)
# #  if ss>= max:
# #   index = x
# #   max =ss


# # pprint(sentence,width=10)



# ###################
# # class Point :
# #  color="red"
# #  def __init__(self,x,y):
# #   self.x=x
# #   self.y=y
# #  def myPrint(self):
# #    print(self.x,self.y)
# #  @classmethod
# #  def setcolor(cls,newcolor):
# #   cls.color=newcolor
# #   return cls.color
# # point=Point(1,2) 
# # point.z=5 
# # print(point.z)
# # Point.color="pink"
# # print(Point.color)  # prints: pink
# # dd=Point(3,4)
# # dd.myPrint()
# # point.color="blue"
# # print(Point.color)
# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

#     # def __str__(self):
#     #     return f"Person({self.name}, {self.age})"

#     # def __repr__(self):
#     #     return f"Person('{self.name}', {self.age})"

# # person = Person("Ali", 30)
# # print( repr(person) )     # يُظهر: Person(Ali, 30)




# # class Point:
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y

# #     def __add__(self, other):
# #         return Point(self.x + other.x, self.y + other.y)

# # p1 = Point(1, 2)
# # p2 = Point(3, 4)
# # p3= Point(1,1)
# # result = p1 + p2 + p3
# # print(result)  # يُظهر: 4 6


# # class Dect:
# #     decti={}
# #     def __init__(self):
# #         self.decti={}
# # obj = Dect()
# # obj.decti.get()     


# # dd=[[1,2],[3,4]]
# # for i in dd:
# #  print(" ".join(str(j) for j in i))
    

# # import tkinter as tk

# # # إنشاء نافذة
# # window = tk.Tk()
# # window.title("Increase Counter")

# # # المتغير الذي نريد زيادته
# # counter = 0

# # # دالة لزيادة قيمة المتغير وعرضها
# # def increase_counter():
# #     global counter
# #     counter += 1
# #     label.config(text=f"Counter: {counter}")

# # # إنشاء زر لزيادة المتغير
# # button = tk.Button(window, text="Increase", command=increase_counter)
# # button.pack(pady=10)

# # # عرض قيمة المتغير
# # label = tk.Label(window, text=f"Counter: {counter}")
# # label.pack()

# # # تشغيل النافذة
# # window.mainloop()
# # import keyboard

# # # تعريف المتغير
# # counter = 0

# # def increase_counter():
# #     global counter
# #     counter += 1
# #     print("Counter:", counter)

# # # الاستماع للضغط على المفتاح "n"
# # keyboard.add_hotkey('n', increase_counter)

# # print("Press 'n' to increase the counter. Press 'esc' to exit.")
# # # الانتظار حتى يضغط المستخدم على زر "Esc" للخروج
# # keyboard.wait('esc')

# ddd={(1,2):True,(23,3):False,(5,6):False}
# for item,(point,can) in enumerate(ddd.items()):
#     min=0
#     if point[0]>min:
     

# (0, (6, 2))
# (1, (7, 3))
# (2, (8, 4))
# (3, (9, 5))
# store={}
# store[(x,y)]=de
# print(store)
# pairs=[(6,2),(7,3),(8,4),(9,5)]
# dd=[]  
# for index,pair in enumerate(pairs):
#      if pair[0]==8:
#       d= index
#       goal= pairs.pop(d)
#       print(pairs)
# for index, pair in enumerate(pairs):      
#       dd.append(pair[1])
     
# print(dd)
# print(pairs)
#         print(pair[0])
#         pairs.
# dd=[1,2,3]
# goal1=dd[0]
# goal2=dd[1]
# goal3=dd[2]
# print(goal1,goal2,goal3)
# print(dd)
# sett={1,3,4}
# dd=list(sett)
# print(dd[0],sett)
# ddd={(1,2):True,(3,4):False}


# print(len(ddd))    
# pointFromOldState=[[1,2],[3,4]]
# pointFromNewState=[[1,2],[34,4]]
     
# if pointFromNewState == pointFromOldState :
#         print("equal")
# x=[1,2,3]
# if 1  in x :

#  print(x)
# from collections import deque
# queue=deque([])
# queue.append("A")
# queue.append("b")
# queue.append("c")
# queue.popleft()
# print(queue)
# grid = [[1, 0, 0],
#         [0, 1, 0],
#         [0, 0, 1]]

# # تحويل الشبكة إلى tuple of tuples لتصبح قابلة للتجزئة
# hashable_grid = tuple(map(tuple, grid))

# # إضافة الشبكة إلى set
# visited_states = set()
# visited_states.add(hashable_grid)

# print(visited_states)
# from collections import Counter

# def has_duplicates(lst):
#     counts = Counter(lst)
# #     print(counts)
#     return any(count > 1 for count in counts.values())

# # Example usage
# my_list = ["R", "F", "R",]
# # print(has_duplicates(my_list))  # Output: True

# dd=Counter(d for d in my_list)
# s=1e20
# print(s)
dd={(3, 5): 'R', (2, 6): 'B'}
ddd=(2, 6)
print(ddd[0])
