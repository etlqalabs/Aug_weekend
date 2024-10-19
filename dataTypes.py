
'''def display():
    print("start....")
    for x in range(10):
        print(" i am inside display fun","hello")
    print("end ....")
display() '''
from typing import List

'''rollnum = 10
name = "etl qa labs"
#print(rollnum,name)
print( 'datatype for rollnum: ', type(rollnum))
print(  'datatype for name: ',type(name)) '''

'''
num1 = "10"
num2 = "2010"
print(num1+num2)
print(int(num1)+int(num2))
print(float(num1))

num3 = 1010
con_str =str(num3)
print(type(con_str))

# variable naming convention
# camel case
numberOfStudent = 10

#Pascal case
NumberOfStudent = 10

# snake case
number_of_student = 10

# text = str
# numberic = int,float
# Sequence datatype
'''


'''
name  = "etl1qa2labs"
l = len(name)
print("lenght of string ",l)
for i in range(l):
    item = name[i]
    print(item," : " ,type(item))
    
'''

'''
# LIST
#n(n+1)/2 = 6*7/2 = 21
mark_of_student =[1,2,3,4,5,6]
l = len(mark_of_student)
sum =0
for x in range(l):
    sum = sum + mark_of_student[x]
print(sum)
'''
'''
# Tuple
mark_of_student_tuple =(1,2,3,4,5,6)
mark_of_student_List =[1,2,2,3,4,5,6,6]
mark_of_student_Set ={1,2,3,4,5,6,2}
print(type(mark_of_student_tuple))
print(type(mark_of_student_List))
print(type(mark_of_student_Set))

print("List before : " ,mark_of_student_List)
mark_of_student_List[0] = 10
print("List after : " ,mark_of_student_List)

#print("Tuple before : " ,mark_of_student_tuple)
#mark_of_student_tuple[0] = 10
#print(" Tuple after : " ,mark_of_student_tuple)

print("Set before : " ,mark_of_student_Set)
print("Set after : " ,mark_of_student_Set)

'''

'''
mark_of_student_tuple =(1,2,3,4,5,6)
print(mark_of_student_tuple,"  ",type(mark_of_student_tuple))
mark_of_student_list = list(mark_of_student_tuple)
mark_of_student_list[0] = 10
print(mark_of_student_list,"  ",type(mark_of_student_list))
mark_of_student_tupl1 = tuple(mark_of_student_list)
print(mark_of_student_tupl1,"  ",type(mark_of_student_tupl1))

'''
'''
# dictionary

emp_dict = {"1":"Ram","2":"Shyam"}
print(emp_dict["2"])



# String
str = "etlqalabs"
print(str)

result  = str[0]+str[1]+str[2]
#print(result)
l = len(str)
result_slice = str[0:l:2]
print(result_slice)


s = "hello"
for ch in s:
    print(ord(ch))
''''''


def count_elements(input_list):
    counts = {}
    for element in input_list:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts

# Example usage:
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
result = count_elements(my_list)
print(result)














