#######  all unique - true/false #######
def all_unique(lst):
    return len(lst) == len(set(lst))


x = [1,1,2,2,3,2,3,4,5,6]
y = [1,2,3,4,5]
all_unique(x) # False
all_unique(y) # True


#######  anagrams? #######
from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)


anagram("abcd3", "3acdb") # True


####### object memory use #######
import sys

variable = 30
print(sys.getsizeof(variable)) # 2


####### return length in bytes #######
def byte_size(string):
    return (len(string.encode('utf-8')))


byte_size('😀')  # 4
byte_size('Hello World')  # 11


####### capitalize first letters #######
s = "programming is awesome"

print(s.title()) # Programming Is Awesome

####### list into smaller list #######
def chunk(list, size):
    return [list[i:i+size] for i in range(0,len(list), size)]

####### removes false values #######
def compact(lst):
    return list(filter(None, lst))


compact([0, 1, False, 2, '', 3, 'a', 's', 34])  # [ 1, 2, 3, 'a', 's', 34 ]


####### transpose 2d array #######
array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
print(transposed) # [('a', 'c', 'e'), ('b', 'd', 'f')]


####### get vowels #######
def get_vowels(string):
    return [each for each in string if each in 'aeiou']


get_vowels('foobar') # ['o', 'o', 'a']
get_vowels('gym') # []


####### decapitalize #######
def decapitalize(str):
    return str[:1].lower() + str[1:]


decapitalize('FooBar')  # 'fooBar'
decapitalize('FooBar')  # 'fooBar'


####### flaten list #######
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(xs):
    flat_list = []
    [flat_list.extend(deep_flatten(x)) for x in xs] if isinstance(xs, list) else flat_list.append(xs)
    return flat_list


deep_flatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]


####### variable difference #######
def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)


difference([1,2,3], [1,2,4]) # [3]


####### difference after applying func #######
def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


from math import floor
difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x']) # [ { x: 2 } ]



####### chain function #######
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a, b = 4, 5
print((subtract if a > b else add)(a, b)) # 9


####### has duplicates #######
def has_duplicates(lst):
    return len(lst) != len(set(lst))


x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x)  # True
has_duplicates(y)  # False


####### merge dictionaries #######
def merge_dictionaries(a, b):
   return {**a, **b}


a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_dictionaries(a, b)) # {'y': 3, 'x': 1, 'z': 4}


####### convert 2 list to dict #######
def to_dictionary(keys, values):
    return dict(zip(keys, values))


keys = ["a", "b", "c"]
values = [2, 3, 4]
print(to_dictionary(keys, values))  # {'a': 2, 'c': 4, 'b': 3}

####### enumerate #######
list = ["a", "b", "c", "d"]
for index, element in enumerate(list):
    print("Value", element, "Index ", index, )
# ('Value', 'a', 'Index ', 0)
# ('Value', 'b', 'Index ', 1)
#('Value', 'c', 'Index ', 2)
# ('Value', 'd', 'Index ', 3)


####### time spent #######
import time

start_time = time.time()

a = 1
b = 2
c = a + b
print(c) #3

end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)

# ('Time: ', 1.1205673217773438e-05)


####### try else #######
try:
    2*3
except TypeError:
    print("An exception was raised")
else:
    print("Thank God, no exceptions were raised.")

#Thank God, no exceptions were raised.


####### most frequent #######
def most_frequent(list):
    return max(set(list), key=list.count)


numbers = [1, 2, 1, 2, 3, 2, 1, 4, 2]
most_frequent(numbers)


####### palindrome #######
def palindrome(a):
    return a == a[::-1]


palindrome('mom') # True


####### calculate without if-else #######
import operator
action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow
}
print(action['-'](50, 25)) # 25


####### shuffle #######
from random import shuffle

foo = [1, 2, 3, 4]
shuffle(foo)
print(foo) # [1, 4, 3, 2] , foo = [1, 2, 3, 4]


####### spread #######
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


spread([1,2,3,[4,5,6],[7],8,9]) # [1,2,3,4,5,6,7,8,9]


####### swap values #######
a, b = -1, 14
a, b = b, a

print(a) # 14
print(b) # -1


####### default values, missing keys #######
d = {'a': 1, 'b': 2}

print(d.get('c', 3)) # 3