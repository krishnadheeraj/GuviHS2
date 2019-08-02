n,k=input().split()
n=int(n)
k=int(k)
x=[]
y=[]
for i in range(n):
  x1=int(input())
  x.append(x1)
for i in range(1,k+1):
  y.append(max(x))
  x.remove(max(x))
print(y[-1])
  
