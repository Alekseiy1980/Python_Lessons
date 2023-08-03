from random import randint

def square(sp):
    res = []
    for item in sp:
        res.append(item**2)
    return res

# sp = [1,4,18,2,9]
sp = [randint(1,10) for _ in range(10)]
print(sp)
print(sum(sp))
print(square(sp))
print([item**2 for item in sp])