# wap to fill name and date in following string

letter = '''Dear <|name|>,
You are selected!
<|date|>'''

letter = letter.replace("<|name|>" , "Shashi").replace("<|date|>","22 Aug 2025")
print(letter)