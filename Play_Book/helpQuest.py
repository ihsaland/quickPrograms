open_list = ['(','{','[']
close_list = [')','}',']']

stack = []
def balance(arr):
    for i in arr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if (len(stack) > 0):
                (open_list[pos] == stack[len(stack) - 1]) #key functionality
            else:
                print("Invalid")

    if len(stack) == 0:
        print("Valid")
    else:
        print("Invalid")

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr =[]

    for _ in range(arr_count):
        arr_item = input()
        arr.append(arr_item)

    balance(arr)
'''
#sum of 2 in matrix
import numpy as np

def pairs(s, matrix):
    stack = []
    for i in matrix:
        if i not in stack: #consider binary tree
            stack.append(i)
            for j in range(i + 1, len(matrix)):
                if i + j == s:
                    print(i,'+', j,'=', s)

if __name__ == '__main__':
    matrix = np.array([[3,0],[4,5],[1,8],[4,2]])
    flatX = matrix.flatten()

    pairs(9,flatX)

#hash table dict
dict = {'key':{'subkey':'value'},'k2':'v2'}
print(dict)

dict['k3'] = 1
print(dict)

del dict['k2']
print(dict)

#binary tree
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.insert(123)
root.insert(55)
root.insert(91)

root.PrintTree()

      
#Linked List
#https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3


#stacks
#https://www.geeksforgeeks.org/stack-in-python/
stack = []
stack.append('a')
print(stack)
stack.pop('a')
print(stack)


#hash table
#https://www.edureka.co/blog/hash-tables-and-hashmaps-in-python/

my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
print(my_dict)
type(my_dict)

#or

new_dict=dict()
print(new_dict)
type(new_dict)

#kth largest element
#https://leetcode.com/problems/kth-largest-element-in-an-array/

#read/write disk IO optimization
#https://towardsdatascience.com/optimized-i-o-operations-in-python-194f856210e0

#load balance during peak workloads
#https://aws.amazon.com/elasticloadbalancing/?elb-whats-new.sort-by=item.additionalFields.postDateTime&elb-whats-new.sort-order=desc

#performance bottlenecks 3 tier architecture
#https://theassyrianblog.wordpress.com/devops/debug-3-tier-bottlenecks/
'''
