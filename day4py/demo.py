# # postive and negative number
# n=int(input("enter the value"))
# if n>0:
#     print("positive")
# elif n<0:
#     print("negative")
# else:
#     print("zero")


# # anagram
# def isAnagram(s,t):
#     if len(s)!= len(t):
#         return False
#     return sorted(s)==sorted(t)
# s=input("enter 1st word:")
# t=input("enter 2nd word:")
# print("are they anagram?",isAnagram(s,t))

# # climbing staries
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
        
# #         # Using the iterative Fibonacci approach
#         prev_1, prev_2 = 1, 2
        
#         for i in range(3, n + 1):
#             current = prev_1 + prev_2
#             prev_1 = prev_2
#             prev_2 = current
            
#         return prev_2
# fizzbuzz

# class Solution:
#     def fizzBuzz(self, n: int) -> list[str]:
#         return [("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or str(i)) for i in range(1, n+1)]

# majority number
# nums = [1, 2, 3, 4, 1, 1, 1, 2, 4]

# for num in nums:
#     if nums.count(num) >= len(nums) // 2:
#         print(num)
        # break
# 349

# nums1 = [1,2,2,1]
# nums2 = [2,2]

# result = []

# for num in nums1:
#     if num in nums2 and num not in result:
#         result.append(num)

# print(result)
# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]

# result = []
# intersectuion 
# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]

# result = []

# i = 0
# while i < len(nums1):
#     j = 0
#     while j < len(nums2):
#         if nums1[i] == nums2[j]:      # check common element
#             if nums1[i] not in result:   # avoid duplicate
#                 result.append(nums1[i])
#         j += 1
#     i += 1

# print(result)

# union two array

# nums1 = [1, 2, 2, 3]
# nums2 = [2, 3, 4, 5]

# result = []

# for num in nums1:
#     if num not in result:
#         result.append(num)

# for num in nums2:
#     if num not in result:
#         result.append(num)

# print(result)
# merge two array
# list1 = [1, 2, 4]
# list2 = [1, 3, 4]

# result = []

# i = 0
# j = 0

# while i < len(list1) and j < len(list2):
#     if list1[i] < list2[j]:
#         result.append(list1[i])
#         i += 1
#     else:
#         result.append(list2[j])
#         j += 1
# while i < len(list1):
#     result.append(list1[i])
#     i += 1

# while j < len(list2):
#     result.append(list2[j])
#     j += 1

# print(result)

# merge sorted array
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# i = m - 1
# j = n - 1
# k = m + n - 1

# while i >= 0 and j >= 0:
#     if nums1[i] > nums2[j]:
#         nums1[k] = nums1[i]
#         i -= 1
#     else:
#         nums1[k] = nums2[j]
#         j -= 1
#     k -= 1

# while j >= 0:
#     nums1[k] = nums2[j]
#     j -= 1
#     k -= 1

# print(nums1)
# longest common prefix
# str_input = input("Enter words separated by space: ")
# strs = str_input.split()

# prefix = ""
# if len(strs) > 0:
#     for i in range(len(strs[0])):
#         char = strs[0][i]
#         for word in strs:
#             if i >= len(word) or word[i] != char:
#                 print("Longest Common Prefix:", prefix)
#                 exit()
        
#         prefix += char
# print("Longest Common Prefix:", prefix)

# add digits

# num = int(input("Enter a number: "))

# while num >= 10:
#     total = 0
#     for digit in str(num):
#         total += int(digit)
#     num = total

# print("Result:", num)

# # reveras
# s = ["h","e","l","l","o"]
# left = 0
# right = len(s) - 1
# while left < right:
#     s[left], s[right] = s[right], s[left]
#     left += 1
#     right -= 1
# print(s)
# single numbers

# nums = [4,1,2,1,2]

# result = 0

# for num in nums:
#     result = result ^ num

# print("Single Number:", result)

# insert values
# nums = [3, 2, 2, 3]
# val = 3

# k = 0   

# for i in range(len(nums)):
#     if nums[i] != val:
#         nums[k] = nums[i]
#         k += 1

# print("k =", k)
# print("Modified array =", nums[:k])

# moves zero 
nums = [0, 1, 0, 3, 12]
k = 0  
for i in range(len(nums)):
    if nums[i] != 0:
        nums[k] = nums[i]
        k += 1
for i in range(k, len(nums)):
    nums[i] = 0
print(nums)














