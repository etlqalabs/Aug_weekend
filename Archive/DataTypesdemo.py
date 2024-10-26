'''
List1 = [1,2,100.6,["Ram","Shyam"],("Mahesh","Suresh"),{"Amar","veer"},{"1":"Mukesh","2":"Shankar"}]
for item in List1:
    print(item," : ",type(item))
'''

'''
String gradefunc(){
 return grade
}

void display(){
print("hello")
}

'''
'''
def display():
    print("abc")
    print("abc")
    for i in range(10):
        print(i)
        
 
# write a function to return the grade based o percentage

def getGrade(perc):
    if perc < 35:
        grade = "FAIL"
    elif perc >= 35 and perc <= 50:
        grade = "Third Division"
    elif perc > 50 and perc < 65:
        grade = "Second Division"
    else:
        grade = "First Division"
    return grade

perc = input("Enter the percentage")
print(" The grade is : ",getGrade(int(perc)))
'''

#Write a function to return the common elements from 2 different sets
def getCommonElements(set1,set2):
    set3 =  set1 & set2  # & works like a interection in set theory
    return set3
set1 = {1,2,3,4}
set2 = {1,6,5,3,2}
ans = getCommonElements(set1,set2)
print("common elements from two sets are : ",ans)
