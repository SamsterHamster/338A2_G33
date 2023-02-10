import json
import sys
import timeit
from urllib.request import urlopen
import numpy as np
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    stack = []
    stack.append((low, high))
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = func2(arr, low, high)
            stack.append((low, pi-1))
            stack.append((pi+1, high))

def func2(arr, start, end):
    p = arr[start]
    low = start + 1
    high = end
    while True:
        while low <= high and arr[high] >= p:
            high -= 1
        while low <= high and arr[low] <= p:
            low += 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    arr[start], arr[high] = arr[high], arr[start]
    return high

url = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json"
response = urlopen(url)
data = json.loads(response.read())

times = []
for x in range(len(data)):
    times.append(timeit.timeit(lambda: func1(data[x], 0, len(data[x])-1), number=1))
    x += 1

#print(times)


# data to be plotted
x = []
for i in range(1000, 10001, 1000):
    x.append(i)
    i+=1

x = np.array(x)
y = np.array(times)

# plotting
plt.xlabel("n")
plt.ylabel("time (s)")
plt.plot(x, y, color ="red", label="line")
plt.title("ex2.4")
plt.savefig("ex2.4Graph.jpg")
