# # pascal triangle
# numRows = int(input("Enter number of rows: "))

# triangle = []

# for i in range(numRows):
#     row = [1] * (i + 1)   

#     for j in range(1, i):
#         row[j] = triangle[i-1][j-1] + triangle[i-1][j]

#     triangle.append(row)

# print(triangle)

# pacel traiangle2
# rowIndex = int(input("Enter row index: "))

# row = [1] * (rowIndex + 1)

# for i in range(2, rowIndex + 1):
#     for j in range(i - 1, 0, -1):
#         row[j] = row[j] + row[j - 1]

# print(row)

# roman to interger

# s = input("Enter Roman numeral: ").upper()
# values = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000
# }
# total = 0
# i = 0
# while i < len(s):
#     if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
#         total = total + values[s[i + 1]] - values[s[i]]
#         i = i + 2
#     else:
#         total = total + values[s[i]]
#         i = i + 1
# print("Integer value:", total)
# maximun product of three
# nums = list(map(int, input("Enter numbers separated by space: ").split()))
# max1 = max2 = max3 = float('-inf')
# min1 = min2 = float('inf')
# for n in nums:
#     if n > max1:
#         max3 = max2
#         max2 = max1
#         max1 = n
#     elif n > max2:
#         max3 = max2
#         max2 = n
#     elif n > max3:
#         max3 = n
#     if n < min1:
#         min2 = min1
#         min1 = n
#     elif n < min2:
#         min2 = n
# product1 = max1 * max2 * max3
# product2 = min1 * min2 * max1
# print("Maximum product:", max(product1, product2))
# remove duplicate
# nums = list(map(int, input("Enter sorted numbers: ").split()))
# if len(nums) == 0:
#     print("Unique count: 0")
# else:
#     i = 0   
#     for j in range(1, len(nums)):
#         if nums[j] != nums[i]:
#             i += 1
#             nums[i] = nums[j]
#     print("Unique count:", i + 1)
#     print("Array after removing duplicates:", nums[:i+1])

# deletaed captial letter
word = input("Enter a word: ")

if word.isupper() or word.islower() or word.istitle():
    print(True)
else:
    print(False)