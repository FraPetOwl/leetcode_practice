# Python Capabilities: Beginner to Advanced
# --------------------------------------------------

# BASIC SYNTAX
print("Hello, World!")

# VARIABLES
x = 5
y = 3.14
name = "Alice"
is_active = True

# DATA TYPES AND TYPE CASTING
print(int(y))
print(float(x))
print(str(x))
print(type(name))

# MATH OPERATIONS
print(x + y)
print(x ** 2)
print(x % 2)

# STRING OPERATIONS
print(name.upper())
print(name.lower())
print("Hello " + name)
print(f"{name} is {x} years old")

# LISTS
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
print(fruits[1])

# FOR LOOPS
# Looping with index
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# Looping with enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Looping with condition
for fruit in fruits:
    if fruit.startswith("b"):
        print(f"Starts with b: {fruit}")

# TUPLES
coordinates = (10, 20)
print(coordinates[0])

# DICTIONARIES
person = {"name": "Alice", "age": 25}
print(person["name"])
person["age"] += 1

# SETS
unique_numbers = {1, 2, 3, 2}
unique_numbers.add(4)
print(unique_numbers)

# CONDITIONALS
if x > 3:
    print("x is greater than 3")
elif x == 3:
    print("x is 3")
else:
    print("x is less than 3")

# WHILE LOOPS
while x > 0:
    print(x)
    x -= 1

# FUNCTIONS
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))

# LAMBDA FUNCTIONS
square = lambda n: n ** 2
print(square(5))

# LIST COMPREHENSION
squares = [n ** 2 for n in range(10)]
print(squares)

# Filtering even numbers
evens = [n for n in range(10) if n % 2 == 0]
print(evens)

# Nested list comprehension (matrix flattening)
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)

# SLICING LISTS / ARRAYS
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first_three = arr[:3]      # First 3 elements
next_three = arr[3:6]      # Next 3 elements
last_three = arr[-3:]      # Last 3 elements
step_two = arr[::2]        # Every second element
print("First 3:", first_three)
print("Next 3:", next_three)
print("Last 3:", last_three)
print("Step 2:", step_two)

# EXCEPTION HANDLING
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("Done")

# CLASSES AND OBJECTS
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} says woof!")

fido = Dog("Fido")
fido.bark()

# FILE I/O
with open("example.txt", "w") as f:
    f.write("Hello file!")

with open("example.txt", "r") as f:
    print(f.read())

# MODULES
import math
print(math.sqrt(16))

# RANDOM
import random
print(random.randint(1, 10))

# DATETIME
import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# JSON
import json
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)
print(json_str)
print(json.loads(json_str))

# ITERATORS
nums = iter([1, 2, 3])
print(next(nums))
print(next(nums))

# GENERATORS
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)

# DECORATORS
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hi():
    print("Hi!")

say_hi()

# CONTEXT MANAGER
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with ManagedFile("context.txt") as f:
    f.write("Managed file.")

# ASYNCIO
import asyncio

async def say_after(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    await asyncio.gather(say_after(1, "Hello"), say_after(2, "World"))

# asyncio.run(main())  # Uncomment to run async example

# UNIT TESTING
import unittest
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)

# if __name__ == '__main__':
#     unittest.main()  # Uncomment to run unit test

# ADVANCED: MULTIPROCESSING
from multiprocessing import Process

def print_nums():
    for i in range(5):
        print(i)

# p = Process(target=print_nums)
# p.start()
# p.join()  # Uncomment to run multiprocessing example

# ADVANCED: THREADING
import threading

def thread_function():
    print("Thread running")

# thread = threading.Thread(target=thread_function)
# thread.start()
# thread.join()  # Uncomment to run threading example

# ADVANCED: REGEX
import re
pattern = r"\d+"
match = re.findall(pattern, "There are 24 apples and 42 oranges.")
print(match)

# DATA STRUCTURES (INTERVIEW-FOCUSED)

# LINKED LIST
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3)))
print_linked_list(head)

# STACK
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop() if self.stack else None
    def peek(self):
        return self.stack[-1] if self.stack else None
    def is_empty(self):
        return not self.stack

s = Stack()
s.push(1)
s.push(2)
print(s.pop())

# QUEUE
from collections import deque
q = deque()
q.append(1)
q.append(2)
print(q.popleft())

# BINARY TREE
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
inorder(root)

# GRAPH (adjacency list + BFS)
from collections import defaultdict

graph = defaultdict(list)
graph[0].append(1)
graph[0].append(2)
graph[1].append(2)
graph[2].append(0)
graph[2].append(3)
graph[3].append(3)

visited = set()
def bfs(start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])

bfs(2)

# HEAP (priority queue)
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heapq.heappop(heap))

# TRIE
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))  # False

# END OF DEMO
