import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
""" for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1) 

    runtime: 10.233119010925293 seconds        
            """

b_tree = BinarySearchTree(names_1[0])

for name in names_1[1:]:
    b_tree.insert(name)

for name in names_2:
    if b_tree.contains(name):
        duplicates.append(name)

# runtime: 0.2348649501800537 seconds
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
