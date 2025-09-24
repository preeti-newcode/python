import datetime
letter='''
Dear <|name|>,
You are selected!
<|Date|>
'''

name=input("Enter Your Name: ").title()
Date=str(datetime.date.today())

letter=letter.replace('<|name|>',name).replace('<|Date|>',Date)

print(letter)
