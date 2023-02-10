import numpy as np
import matplotlib.pyplot as plt
import sys
from urllib.request import urlopen
import json
import timeit

sys.setrecursionlimit(20000)


def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high



url = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json"
response = urlopen(url)
data = json.loads(response.read())

def sort_func(data, i):
    quarter = int(len(data[i])/4)
    func1(data[i], 0, quarter+1)
    func1(data[i], quarter-1, quarter*2+1)
    func1(data[i], quarter*2-1, quarter*3+1)
    func1(data[i], quarter*3-1, len(data[i])-1)
    
times = []

for x in range(len(data)):
    times.append(timeit.timeit(lambda: sort_func(data, x), number=1))
    x += 1
 
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
plt.plot(x, y, color ="red")
plt.title("ex2.2")
plt.savefig("ex2.2Graph.jpg")