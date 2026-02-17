#task1

# students_type=int(input("enter 1 for hosteller enter 2 for dayscholar"))
# if students_type==1:
#     hostel_fee=int(input("enter ypur hostel fee"))
#     tuition_fee=int(input("enter your tuition fee"))
#     print("total amount you want to pay",hostel_fee+tuition_fee)
# elif students_type==2:
#     tuition_fee=int(input("enter your tuition fee"))
#     bus_fee=int(input("enter the bus fee"))
#     print("total amount you want to pay",bus_fee+tuition_fee)
# else:
#     print("lnvalid input")


# task2

# account_balance=int(input("enter the value"))
# withdrrawal_amount=10000
# if(withdrrawal_amount>=10000):
#     print("insufficient funds")
# elif(withdrrawal_amount>10000):
#     print("limit exceeded")
# else:
#     print("allow withdrawal")

# # task3

# account_balance=100000
# atm_pin=1234
# pin=int(input("enter the pin number"))
# if(pin==atm_pin):
#     print("continue")
# else:
#     print("wrong pin")
# withdrawal_amount=int(input("enter the amount"))
# if(withdrawal_amount>=account_balance):
#     print("valid amount")
# elif(withdrawal_amount>0 and withdrawal_amount<=account_balance):
#     print("valid withdrawal")
# else:
#     print("withdrawal successful")
# amount=int(input("enter the amount"))
# if(amount>account_balance):
#     print("insufficient balance")
# else:
#     print("balance is insufficient")
    
# task4
# age=int(input("enter the value"))
# if age<=5:
#     print("free entry")
# elif 5<= age <=17:
#     print("child ticket price ₹150")
# elif age>60:
#     print("senior citizen price ₹250")
# elif 18<= age >=59:
#     print("normal ticket price ₹150")
# else:
#     print("no entry")
# show_time=int(input("enter 1 for morning show  enter 2 for evening show"))
# if show_time==1:
#     print("₹50 discount for morning show")
# else:
#     print("normal price")


#LOOP

# # task1
# sum=0
# for i in range(1,100,2):
#     print(i)
#     sum=i+sum
# print(sum)

# # task2
# sum=0
# for i in range (2,100,2):
#     print(i)
#     sum=i+sum
# print(sum)

# task3
# n=int(input())
# for i in range (1,10):
#     print(i+n)

# task 5
# for i in range (1):
#     print("*",end="")
# print()
# for i in range (2):
#     print("*",end="")
# print()
# for i in range (3):
#     print("*",end="")
# print()
# for i in range (4):
#     print("*",end="")
# print()
# for i in range (5):
#     print("*",end="")
# print()

# task5

# for i in range (5):
#     print("*",end="")
# print()
# for i in range (4):
#     print("*",end="")
# print()
# for i in range (3):
#     print("*",end="")
# print()
# for i in range (2):
#     print("*",end="")
# print()
# for i in range (1):
#     print("*",end="")
# print()

# task6

# tm=int(input("tm:"))
# eng=int(input("eng:"))
# maths=int(input("maths:"))
# sci=int(input("sci:"))
# soc=int(input("soc:"))
# total=tm+eng+maths+sci+soc
# print(total)
# avaerage=total/2
# print("pass")

# task 7
# i=1
# odd=0
# while i<=10:
#     odd +=1
#     i+=1
# print(odd)

# task 8
# i=0
# while i<=10:
#     if i%2==0:
#         print(i)
#     i+=1

# task 9
total_seats=30
start_seat=1
while(start_seat<=total_seats):
    name=int(input("enter passenger name"))
    print(f"seat {start_seat} booked for{name}\n")
start_seat +=1
print("all the seat are")







        


    


