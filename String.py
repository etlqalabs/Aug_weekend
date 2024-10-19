# print the elelemts from the string
s1 ="etlqa"
'''
# Way 1 
#for ch in s1:
#    print(ch)

# Way 2
length = len(s1)
print(length)
for idx in range(length):
    print(idx,":  ",s1[idx])

# way 3
# s1 = "etlqa"
i = 0
length = len(s1)  # 5
while (i < length):
    print(s1[i])
    i = i + 1

# How to revese the words in a string  => WAY 1 
s1 ="etl qa labs"
# expetcted output : labs qa etl
l = s1.split()
# ['etl', 'qa', 'labs']
ans =""
length = len(l) -1  # 3-1 = 2
while length >=0:
    ans = ans + l[length]+" "  # 1st iteration  ans = ""+l[2] = labs
                               # 2nd iteration  ans    = labs + l[1] = labs qa
                               # 3rd iteration         = labs qa + l[0] = labs qa etl
    length = length -1
print(ans)


# How to revese the words in a string  => WAY 2
s1 ="etl qa labs"
l = s1.split()
print(l)
['etl', 'qa', 'labs']
revlist = l[::-1]
print(revlist," ",type(revlist))
ans = " ".join(revlist)
print(ans,type(ans))


# How to sum the ascii values for the given string
# ASCII
s1  = "abc" # 65 + 25 = 90
sum = 0
for ch in s1:
    sum = sum +ord(ch)
print(sum)

s1 = "ETLQALABS"
# output => QALAB
startindex = s1.find('Q')
endtindex = s1.find('B')
ans = s1[startindex:endtindex+1:1]
print(ans)


# Continue
# print the all the even number from 20 to 50
for i in range(20,50):
    if i % 2 != 0:
        continue
    print(i)

# break
# print the all the even number from 20 to 50
for i in range(20,50):
    if i == 40:
        break
    print(i)

# Pass
for i in range(10):
    pass

age = 19
if( age < 18):
    print("Person is not elligible to vote")
elif (age > 18 and age <20 ):
    print("Person is still not elligible to vote")
else:
    print("Person is  elligible to vote")
'''

# function
# define the function
def display():
    print(" i am inside the function : Line 1")
    print(" i am inside the function : Line 2")
    print(" i am inside the function : Line 3")
    print(" i am inside the function : Line 4")

# calling the function
display()
print(" I am outside the function")












