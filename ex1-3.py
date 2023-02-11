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