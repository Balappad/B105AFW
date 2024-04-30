fruits=('apple','banana','apple','mango','orange')
print(fruits.count('apple'))#2
print(fruits.count('mango'))#1
firstapple=fruits.index('apple',0)#0
print(firstapple)
secondapple=fruits.index('apple',firstapple+1)#2
print(secondapple)

