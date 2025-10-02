a=int(input())
series=[0,1]

while a>=series[-1]:
    series.append(series[-1]+series[-2])

l=0
r=len(series)-1
while l<=r:
    h=(l+r)//2
    if series[h]==a:
        print("Found")
        break;
    else:
        if a>series[h]:
            l=h+1
        else:
            r=h-1
else:
    print("Not found")
