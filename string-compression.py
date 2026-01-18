"""Example:
Input: aaabbcddd
Output: a3b2cd3
"""

def Size(word):
    
    a=""
    letter=""
    no=1
    for x in word:
        if x != letter:
            if letter != "" and no>1:
                a=a+letter+str(no)
            elif letter != "" and no==1:
                a=a + letter
            letter=x
            no=1
        else:
            no+=1
    else:
        if no>1:
            return a+letter+str(no)
        else:
            return a+letter
    
    
user=input("Enter characters to return its char+number value\n:")
print(Size(user))
