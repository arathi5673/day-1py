# contains duplicate
# nums = [1, 2, 3, 1]
# seen = set()
# duplicate = False
# for n in nums:
#     if n in seen:
#         duplicate = True
#         break
#     seen.add(n)
# print(duplicate)

# combination 
# from itertools import combinations
# n = 4
# k = 2
# nums = range(1, n + 1)
# result = list(combinations(nums, k))
# print(result)

# power of 2
# n = 16   # change value to test

# if n <= 0:
#     print(False)
# else:
#     while n % 2 == 0:
#         n = n // 2
    
#     print(n == 1)

# power of 4
# n = 16   # Change this value to test

# if n <= 0:
#     print(False)
# else:
#     while n % 4 == 0:
#         n = n // 4
    
#     print(n == 1)

    # power 3
# n = 27 

# if n <= 0:
#     print(False)
# else:
#     while n % 3 == 0:
#         n = n // 3
    
#     print(n == 1)


# class students:
#      def details (self, name,marks):
#          if marks>40:
#             result="pass"
#             print(result)
#             print(name,marks)
#         else:
#             print("fail")
        
        
# s1=students()
# s2=students()
# s1.details("rvs",88)

# # /syntax (witout cons)
# class ClassName:
#      def method_name(self):
#           print("message")

# with (cons)

# class student:
#      def __init__(self,name,marks):
#           self.name=name
#           self.marks=marks
#      def show_result(self):
#           if self.marks>=40:
#                result="pass"
#           else:
#                result="fail"
#           print("\n student name:",self.name)
#           print("marks",self.marks)
#           print("result",result)
# name=input("enter  name:")
# marks=int(input("enter marks:"))
# s1=student(name,marks)
# s1.show_result()

#
class Temperature:
    def __init__(self, celsius_list):
        self.celsius_list = celsius_list
    def convert(self):
        for c in self.celsius_list:
            f = (c * 9/5) + 32
            print(c, "°C =", f, "°F")
values = [10, 20, 50, 40, 10]
t = Temperature(values)
t.convert()