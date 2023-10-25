a = [
    [1,1,1],
    [2,5,8],
    [3,24,63]
]

st = 1 # 0/1/2

if st==0:
    y = 1
    z = 2
elif st==1:
    y = 0
    z = 2
elif st==2:
    y = 0
    z = 1
else:
    "error"


def f(m,x):
    return x*(m[0][0]*m[1][1]-m[0][1]*m[1][0])

b1 = [
    [a[y][1],a[y][2]],
    [a[z][1],a[z][2]]
]
b2 = [
    [a[y][0],a[y][2]],
    [a[z][0],a[z][2]]
]
b3 = [
    [a[y][0],a[y][1]],
    [a[z][0],a[z][1]]
]

if st==1:
    print(-f(b1,a[st][0])+f(b2,a[st][1])-f(b3,a[st][2]))
else:
    print(f(b1,a[st][0])-f(b2,a[st][1])+f(b3,a[st][2]))