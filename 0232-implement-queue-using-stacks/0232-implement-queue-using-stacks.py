# class MyQueue:

#     def __init__(self):
#         self.s1=[]
#         self.s2=[]
        
#     def push(self, x: int) -> None:
#         self.s1.append(x)

#     def pop(self) -> int:
#         self.changetos2()
#         self.s2.pop()

#     def peek(self) -> int:
#         self.changetos2()
#         return self.s2[-1]

#     def empty(self) -> bool:
#         return len(self.s1)==0
 
#     def changetos2(self):
#         if not self.s2:
#             while self.s1:
#                 self.s2.append(self.s1.pop())

# # Your MyQueue object will be instantiated and called as such:
# # obj = MyQueue()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# # param_4 = obj.empty()

class MyQueue(object):

    def __init__(self):
        self.queue = []
        self.tmp = []

    def push(self, x):
        while not len(self.queue) == 0:
            self.tmp.append(self.queue.pop())
        self.queue.append(x)
        while not len(self.tmp) == 0:
            self.queue.append(self.tmp.pop())

    def pop(self):
        return self.queue.pop()
        
    def peek(self):
        return self.queue[len(self.queue)-1]
        
    def empty(self):
        return len(self.queue) == 0
