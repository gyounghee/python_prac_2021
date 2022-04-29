n, m = map(int, input().split())
p = list(map(int, input().split()))

ans = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            total = p[i]+p[j]+p[k]
            if m < total: continue
            else : ans = max(ans, total)
print(ans)

# 별찍기 1
n = 5

for i in range(n):
  for j in range(i+1):
    print('*', end='')
  print()


# 별찍기 2
n = 5
l = [ [' '] * n for _ in range(n) ]

for i in range(n):
    for j in range(i+1):
        l[i][n-1-j] = '*'
    for k in range(n):
        print(l[i][k],end='')
    print()


# 별찍기 3
n = 5
l = [ [' '] * n for _ in range(n) ]

for i in range(n):
    for j in range(n-i):
        l[i][j] = '*'
        print(l[i][j],end='')
    print


# 별찍기 4
n = 5
l = [ [' '] * n for _ in range(n) ]

for i in range(n):
    for j in range(i,n):
        l[i][j] = '*'
    for k in range(n):
        print(l[i][k],end='')
    print()


# 별찍기 5

n = 5
l = [ [' '] * (n*2-1) for _ in range(n) ]
# 5칸 만듦 
for i in range(n):  
    for j in range(n-i-1,n):
        l[i][j]='*'
    for k in range(n-1,n+i): 
        l[i][k] = '*'
    for s in range(n*2-1):
        print(l[i][s],end='') 
    print()
