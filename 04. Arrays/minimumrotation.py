n,m=input().split(" ")
def rotate(n):
    a=n[-1]
    b=n[:-1]
    return (a+b)
n.lower()
m.lower()
z=0
if len(n)!=len(m):
    print (-1)
else:
    for i in range(len(n)):
        z+=1
        n=rotate(n)
        if n==m:
            print(min(z,len(n)-z))
            break
    if z==len(n):
        print(-1)
        
        
        
        