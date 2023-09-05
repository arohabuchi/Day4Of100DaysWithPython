# intro to string datatype: '', ""
strv: str = "hello world"
print(strv)

print(strv[0])
print(strv[0:5])

# intro to set: {}
# set are unique collections of objects. there are to type

# 1. set:mutable
basket = {'banana', 'tomatoes', 'tomatoes', 'pear', 'mango'}
print(basket)
j = set('acacacerddderdsssw')
print('j : ',j)

# 2. frozeset: immutable
b = frozenset("abbcaeeces")
print('b: ',b)

cities = frozenset({"awka","onistcha","owerri","imo","delta","imo","awka","obosi","awada","obosi","enugu","enugu","awka","awka","imo"})
print(cities)

# intro to number datatypes
intNum = 80
floatNum = 90.87
complexNum = 7.89j
longNum = 1234567

# intro to list datatype
li=["hi", 48, 890,9.0,'man','obi','no','ye','winner','pear']
l2=['hello','world']
print(li)
print(li[0:2])
print(li*2)
print(li + l2)

