
import timeit as time
import matplotlib.pyplot  as plt
import pandas as pd


def func(n):
    if  n == 0 or n == 1:
        return n

    else:
        return func(n-1) + func(n-2)


cache = dict()

def newfunc(n):

    if n in cache: 
        return cache[n]
    

    if n == 0 or n == 1:
        return n
    else:
        result = newfunc(n-1) + newfunc(n-2)
        cache[n] = result
        return result

old = list()
new = list()
test = 36
for x in range(test):
    old.append(time.timeit(lambda: func(x), number = 1))
    x += 1

for x in range(test):
    new.append(time.timeit(lambda: newfunc(x), number = 1))
    x += 1

for x in range(test):
    print(f"Time for old code n = {x} is: {old[x]}\n")
    x += 1

for x in range(test):
    print(f"Time for new code n = {x} is: {new[x]}\n" )
    x += 1

numbers = list(range(test))
old_dict = {"n":numbers, "Time":old}
new_dict = {"n":numbers, "Time":new}
old_df= pd.DataFrame(old_dict)
new_df= pd.DataFrame(new_dict)
ax = old_df.plot(x = "n", y = "Time", kind ="line", label = "Old")
new_df.plot(ax=ax,x = "n", y = "Time", kind ="line", label = "New")
plt.savefig("FibonachiTimesGraph.jpg")
