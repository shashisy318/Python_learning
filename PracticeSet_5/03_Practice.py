''' Create an Empty Dict. Allow four friend to input their name as key and 
fav language as value'''

lang = {}

name = input("Enter your name : ")
favLang = input("Enter your favorite language : ")
lang.update({name:favLang})

name = input("Enter your name : ")
favLang = input("Enter your favorite language : ")
lang.update({name:favLang})

name = input("Enter your name : ")
favLang = input("Enter your favorite language : ")
lang.update({name:favLang})

name = input("Enter your name : ")
favLang = input("Enter your favorite language : ")
lang.update({name:favLang})

print(lang)


'''if two name becomes same then the value fav lang will be updated 
as update function updates the value of key if key is already 
present in dictionary'''