x=[1,2,3,4,5]
l=0
r=len(x)-1
while l<r:
    x[1],x[r]=x[r],x[1]
    l+=1
    r-=1
print(x)