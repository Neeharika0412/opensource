n,x,y=map(int,input().strip().split())
if 0<=y <=n*x and y%x==0:
    print("YES")
else:
    print("NO")
