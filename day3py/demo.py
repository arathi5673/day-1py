# fibonacci number 
# n = int(input("Enter number of terms: "))

# a = 0
# b = 1
# i = 0

# while i < n:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     i += 1
              
# tribonacci number
# n= int(input("enter the  number of value:"))
# a=0
# b=1
# c=1
# i=0
# while i<n:
#     print(a,end=" ")
#     d=a+b+c
#     a=b
#     b=c
#     c=d
#     i+=1

# list
# topices 
# list indices,slicing,methods,operatores,map,filter,reduces

# list
# list[1,2,3,4]
# print(list[3])
# # slicing
# print(list[0:3])
# print(list[:2])
# # operatores
# # concatentation 
# a=[1,2,23,56,75]
# b=[78,65,34,3,7]
# print(a+b)
# # repetition opertores
# print(a*2)
# # membership opertores
# print(78 in a)
# print(55 in b)
# # comparison opertores
# print(a==b)
# print(a>b)
# print(b<a)
# print(a<=b)
# print(b>=a)
# list methodes
# append
# num=[1,23,45,9,8]
# num.append(4)
# print(num)
# # insert
# num.insert(8,5)
# print(num)
# # extend
# a=[1,2,34]
# # b=[1,54,89]
# # a.extend(b)
# # print(a)
# # remove
# a.remove(1)
# print(a)
# # pop
# a.pop(1)
# print(a)
# num=[10,2,3,4,2]
# print(num.index(2))
# num[2]
# # count
# print(num.count(2))
# # clern
# num=[1,2,34,6]
# num.clear()
# print(num)
# # sort
# a=[1,2,3,4,5]
# a.sort()
# print(a)
# #reverse
# a.sort(reverse=True)
# print(a)
# a.reverse()
# # copy
# b=a.copy()
# print(b)
# num=[1,2,3,4,5]
# def func(x):
#     return x*2
# resulit=list(map(func,num))
# print(resulit)

# numone=[1,2,3,4,5,6]
# resultone=list(filter(lambda x:x%2==0,numone))
# print(resultone)
# # normal function
# num=[1,2,3,4,5]
# def func(x):
#     return x%2==0
# resulit=list(filter(func,num))
# print(resulit)
# # resuce
# from functools import reduce
# num=[1,2,3,4]
# result=reduce(lambda a,b:a+b,num)
# print(result)

# num=[1,2,3,4,5,6,7,8,9]
# Even_num=list(filter(lambda x:x%2==0,num))
# print(Even_num)
# print("Count of even numbers:", len(Even_num))

# palindrome
a=input("enter the word")
if a==a[::-1]:
    print("yes palindrome")
else:
    print("no palindrome")

    # withou slicing
a=input("enter the vaues")
rev=" "
for ch in a:
    rev=ch+rev
if a==rev:
    print("yes palindrome")
else:
    print("no palindrome")

             