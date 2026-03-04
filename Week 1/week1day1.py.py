# 1. **The Sum of Evens:** Write a function that takes an integer $N$ and
#  returns the sum of all strictly even numbers from 1 to $N$.
def qa1(n):
    Thesum=0
    for i in range(0,n,2):
        Thesum+=i
    return Thesum
qa1(5)

# 2. **Palindrome Checker:** Write a function that returns `True` if a string reads
# the same forwards and backwards (ignoring spaces and case), and `False` otherwise.
def qa2 (str):
    if(str=="".join(reversed(str))):
        return True
    else:
        return False
qa2("bob")

# 3.List Reverser: Reverse a list of numbers without using
# Python's built-in .reverse() method or [::-1] slicing.
def qa3(list):
    reversedlis=[]
    i=len(list)-1
    while i>=0:
        reversedlis.append(list[i])
        i-=1
    return(reversedlis)
qa3([1,2,3,4,5])

# 4.Character Frequency: Take a string and 
# return a dictionary counting how many times each character appears.
def qa4(str):
    dict_of_frequency={}
    for i in range(len(str)):
        dict_of_frequency[str[i]]=str.count(str[i])
    return dict_of_frequency
qa4("pruthviraj")

# 5. **Find the Missing Number:** Given a list containing $n$
# distinct numbers taken from $0, 1, 2, ..., n$, find the one that is missing from the list.
def qa5(lis):
    n = len(lis)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lis)
    return expected_sum - actual_sum
qa5([1,2,3,5,6])

# 6. **Celsius to Fahrenheit:** Write a function that converts a list of Celsius temperatures
# into a new list of Fahrenheit temperatures.
def qa6(celsiusList):
    for i in range(0,len(celsiusList)):
        celsiusList[i]=(celsiusList[i]*(9/5))+32
    return celsiusList
qa6([0,1,2,3,4,5])

# 7. **Remove Duplicates:** Write a function thae keeping the original order of elements intact 
# (don't just convert to a set, as sets lose order).t removes duplicate elements from a list whil
def qa7(list):
    listAns=[]
    for i in list:
        if i not in listAns:
            listAns.append(i)
    return listAns
print(qa7([1,2,4,5,6,6,6,6]))

# 8. **Factorial Calculator:** Write a function using a `while` loop to calculate the factorial of a given 
# number $N$ (e.g., $5! = 5 \times 4 \times 3 \times 2 \times 1$). 
def qa8(num):
    factorial=1
    i=num
    while i>0:
        factorial*=i
        i-=1
    return factorial
print(qa8(5)) 

# 9. **Vowel Remover:** Write a function that takes
#    a string and returns a new string with all the vowels removed.
def qa9(str):
    strlis=list(str)
    for i in strlis:
        if i in "aeiouAEIOU":
            strlis.remove(i)
    return"".join(strlis)
qa9("ram")

# 10. **Target Search:** Iterate through a list of integers. If you find the number `7`,
# print its index and stop the loop. If `7` is not in the list, print "Not found".
def qa10(lst):
    for i in range(len(lst)):
        if lst[i] == 7:
            print(i)
            return
    print("Not found") 