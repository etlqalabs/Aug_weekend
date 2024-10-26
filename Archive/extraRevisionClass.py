# indentation  example
'''
this is example
of
indentation

'''
'''
for x in range(10):
    print(x)
print("helloo")


# Variable is container
channelName = "etlqa labs"
print(channelName)

# List
list1 = [1,2,3,4,5,2]
print("List:" , list1)
print("3rd index value " , list1[3])



# Tuple
tuple1 = (1,2,3,4,5,2)
print("tuple :", tuple1)
print("2nd index of tuple ", tuple1[2])

# Set
set1 = {1,2,3,4,5,2,4}
print("set: ", set1)
list2 = list(set1)
print("2nd index of set ",list2[4])


# Dictionary
dict1 = {"1":"Akshay","2":"Amit","3":"Pankaj","10":"Akash"}
#print(dict1["10"])
dict2 = {"city":"Bangalore","country":"India"}
print(dict2["city"])
# String Slicing

name = "ETLQALABS"
# get the first 5 charcters form the string
SubstringName = name[0:5:1]
#print(name[0:5:1])
print(SubstringName)

# get the substring at all the odd indexes
SubstringName = name[1::2]
#print(name[0:5:1])
print(SubstringName)

# get the substring at all the even indexes
SubstringName = name[0::2]
#print(name[0:5:1])
print(SubstringName)

# Print the entire string in reverse order
name = "ETLQALABS"
SubstringName = name[::-1]
#print(name[0:5:1])
print(SubstringName)
'''
# for loop
name = "ETLQALABS"
'''
print("1:",name[0])
print("2:",name[1])
print("3:",name[2])
print("4:",name[3])
print("5:",name[4])
print("6:",name[5])
print("7:",name[6])
print("8:",name[7])
print("9:",name[8])
'''

num = 1
for ch in name:
    #print(num,": ",ch)
    num = num +1

list1 = [ 1,2,3,4,5,10]
for num1 in list1:
   # print(num1)
   pass

# while loop for infinite loop
#while(True):
    #print("hello")


list2 = [1,2,3,4,5,10]
length = len(list2)
#print(length)  # 6

i = 0
while(i < length ):
    print(list2[i])
    i = i + 1


