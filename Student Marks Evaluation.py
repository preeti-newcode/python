d={'math':0 ,'science':0 ,'hindi':0 }
for x in d.keys():
    d[x]=int(input(f"Marks of {x}:"))
if sum(d.values())/3>=40:
    for y in d.values():
        if y<33:
            print("You failed")
            break
    else:
        print("You Passed")
else:
    print("You failed")
