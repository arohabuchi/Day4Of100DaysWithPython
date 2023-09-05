# intro to string datatype: '', ""
strv: str = "hello world"
print(strv)

print(strv[0]) #print the first character
print(strv[0:5]) #print the first 5 character

# intro to set: {}
# set are unique collections of objects. there are to type

# 1. set:mutable
basket = {'banana', 'tomatoes', 'tomatoes', 'pear', 'mango'}
print(basket) #print the whole set. duplicate are removed
j = set('acacacerddderdsssw') #convert j to set
print('j : ',j) #print the set j

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
print(li*2) #print li twice
print(li + l2) #concatenate li and l2

#dictionary {}
#uses key value pair. can be asess using square bracket[]
dic = {'gender':'male','age':'20'}
print(dic)#print both the keys and values
print(dic['gender']) #print the value of gender male
print(dic.values())# print all the values
print(dic.keys())# print all the keys


# Turple()
# they are immutable
t1 =(1,2,3,34.90,'hi','hello')
t2=('obi', 'importer','exporter')
print(t1)
print(t1[0]) #print first char in t1
print(t1 + t2) #concatenate t1 and t2
