#funcional

def fib(x):
    return fib(x-1) + fib(x-2) if x>=2 else 1 if x==1 else 0

def fact(x):
    return x*fact(x-1) if x>1 else 1

list = [[1,2],[3,4],[5,6]]

result = []

for elem in list:
    x = fib(elem[0])
    y = fact(elem[1])
    result.append([x,y])

print(result)