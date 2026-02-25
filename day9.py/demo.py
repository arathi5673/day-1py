# import heapq

# pq=[]
# heapq.heappush(pq,3)
# heapq.heappush(pq,3)
# heapq.heappush(pq,3)

# print("priority queue",pq)
# print("removed",heapq.heappop(pq))
# print("removed",heapq.heappop(pq))
# print("removed",heapq.heappop(pq))

# import heapq

# pq = []   
# heapq.heappush(pq, (2, "medium task"))
# heapq.heappush(pq, (1, "high task"))
# heapq.heappush(pq, (3, "low task"))
# while pq:
#     priority, task = heapq.heappop(pq)
#     print(priority, task)


# leecode
# 268
# nums = [3, 0, 1]
# n = len(nums)
# total = n * (n + 1) // 2
# array_sum = sum(nums)
# missing = total - array_sum
# print("Missing number is:", missing)

# 83
# nums = [1, 1, 2, 3, 3]
# result = []
# for num in nums:
#     if num not in result:
#         result.append(num)
# print("After removing duplicates:", result)

# 557
s = "Let's take LeetCode contest"
words = s.split(" ")
result = ""
for word in words:
    result = result + word[::-1] + " "
print(result.strip())




