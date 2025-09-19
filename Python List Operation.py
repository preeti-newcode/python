if __name__ == '__main__':
    N = int(input())
    List=[]
    command=[]
    for x in range(N):
        value=input().split()
        command.append(value)
    for value in command:
        if value[0].lower() in ['insert','append']:
            if value[0]=='insert':
                List.insert(int(value[1]),int(value[2]))
            else:
                List.append(int(value[1]))
        
        elif value[0] in ['pop','remove']:
            if value[0].lower()=='remove':
                List.remove(int(value[1]))
            else:
                List.pop()
                
        elif value[0] in ['reverse','sort']:
            if value[0]=='reverse':
                List.reverse()
            else:
                List.sort()
        
        else:
            print(List)
