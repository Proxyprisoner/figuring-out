#leetcode 43
a="248"
b="245"
l=[]
sum=0
a="248"[::-1]
b="245"[::-1]
for i in range(len(a)):
    c=0
    y="0"*i
    for j in range(len(b)):
        x=int(a[j])*int(b[i])+c
        y=y+str(x)[-1]
        c=x//10
    if c > 0:
        y = y + str(c)
    l.append(y[::-1])
for i in range(len(l)):    
    sum+=int(l[i])
print(sum)