# empty playground for tests

def sum(a,b):
    
    return a + b

items = [10, 20, 30, 40, 50]
nums = [5, 10, 15, 20, 25]

l = [x for x in map(sum,items, nums)]

print(l)
