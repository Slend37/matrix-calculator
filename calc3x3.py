a = [
    [int(input),int(input),int(input)],
    [int(input),int(input),int(input)],
    [int(input),int(input),int(input)]
]

def f(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]

b1 = [
    [a[1][1],a[1][2]],
    [a[2][1],a[2][2]]
]
b2 = [
    [a[1][0],a[1][2]],
    [a[2][0],a[2][2]]
]
b3 = [
    [a[1][0],a[1][1]],
    [a[2][0],a[2][1]]
]

print(f(b1)-f(b2)+f(b3))
