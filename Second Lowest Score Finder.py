if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        element=[name,score]
        records.append(element)
    
    marks=[score for name,score in records]
    
    low=min(marks)
    marks=[x for x in marks if x!=low]
    low=min(marks)
    
    secondLowest=[]
    for name,score in records:
        if score==low:
            secondLowest.append(name)
    
    
    for i in sorted(secondLowest):
        print(i)
        
    
