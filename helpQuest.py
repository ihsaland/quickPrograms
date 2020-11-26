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


#binary tree
#https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def PrintTree(self):
        print(self.data)

root = Node(10)

root.PrintTree()


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

