# import random
import sys

def mergesort(array):
    if len(array) <= 1: 
        return array
    mid = len(array) // 2
    left = mergesort(array[ : mid])
    right = mergesort(array[mid : ])
    
    return merge(left, right)
    
# this function sorts arrays while merging them
def merge(left: list , right: list):
    merged = []     # merged array
    i = j = 0       # i: index in left list, j: index in left list
    while i < len(left) and j < len(right):
        # print(f'left: {left}, right: {right}', )
        if left[i] < right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    if i < len(left):
        merged = merged + left[i:]
    elif j < len(right):
        merged = merged + right[j:]
    return merged

# # test the function
# array = random.sample(range(100), 10)
# print(array)

n = int(input())
array =[]
for _ in range(n):
    array.append(int(sys.stdin.readline()))

for x in mergesort(array):
    print(x)