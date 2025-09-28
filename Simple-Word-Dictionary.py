#Gloabal Value
dictionary={
        "Chai-wala":"Tea-vendor",
        "Bindas":"Carefree",
        "Chill":"Relax",
        "Dabba":"Lunch Box",
        "Larka":"Male",
        "Larki":"Female",
        "Masti":"Fun",
        "Dost":"Friend"
    }
#Function
def Word(word):
    word=word.capitalize()
    return dictionary.get(word)
    
#Main Body
print("Options:")
for key in dictionary.keys():
    print(key,end="\t")
find=input("\nMeaning of?\n")
meaning=Word(find)
print(f"{find.capitalize()} => {meaning}")

