# print("Pizza Categories")
# print("1. Normal")
# print("2. Delux")
# category = int(input("Enter your Choice [1 or 2]: "))
# if category == 1:
#     base_price = 400
# else:
#     base_price = 600
# print("\nPizza Types")
# print("1. Veg")
# print("2. Non Veg")
# ptype = int(input("Enter your Choice [1 or 2]: "))
# cheese = int(input("\nEnter Cheese? [1.Yes or 2.No]: "))
# if cheese == 1:
#     extra_cheese = 100
# else:
#     extra_cheese = 0
# topping = int(input("Enter Topping? [1.Yes or 2.No]: "))
# if topping == 1:
#     extra_topping = 100
# else:
#     extra_topping = 0
# water = int(input("Do you want Water Bottles? [1.Yes or 2.No]: "))
# if water == 1:
#     bottles = int(input("How many bottles?: "))
#     water_cost = bottles * 20
# else:
#     water_cost = 0
# ketchup = int(input("Do you want Ketchup? [1.Yes or 2.No]: "))
# if ketchup == 1:
#     packets = int(input("How many Packets?: "))
#     ketchup_cost = packets * 5
# else:
#     ketchup_cost = 0
# drink = int(input("Do you want Soft Drinks? [1.Yes or 2.No]: "))
# if drink == 1:
#     cans = int(input("How many Cans?: "))
#     drink_cost = cans * 75
# else:
#     drink_cost = 0
# takeaway = int(input("Is it a Take Away? [1.Yes or 2.No]: "))
# if takeaway == 1:
#     takeaway_charge = 20
# else:
#     takeaway_charge = 0
# total = (base_price + extra_cheese + extra_topping +
#          water_cost + ketchup_cost + drink_cost + takeaway_charge)

# gst = total * 0.18
# net_amount = total + gst
# print("\n------ Pizza Bill Generator ------")
# print("Base Price =", base_price)
# print("Extra Cheese =", extra_cheese)
# print("Extra Toppings =", extra_topping)
# print("Water Bottle =", water_cost)
# print("Ketchup Packets =", ketchup_cost)
# print("Soft Drinks =", drink_cost)
# print("Take Away Charges =", takeaway_charge)
# print("-----------------------------------")
# print("Total Cost =", total)
# print("GST Charges =", round(gst, 2))
# print("-----------------------------------")
# print("Net Amount Payable =", round(net_amount, 2))

# stack=[]

# while True:
#     print("\n1.push 2.pop 3.peek 4.display 5.exit")
#     choice=int(input("enter choice:"))
#     if choice==1:
#         val=int(input("enter value"))
#         stack.append(val)
#         print("pushed",val)
#     elif choice==2:
#         if not stack:
#             print("stack empty")
#         else:
#             print("poped",stack.pop())
#     elif choice==3:
#         if not stack:
#             print("stack empty")
#         else:
#             print("top")
#     elif choice==4:
#         print("stack",stack)
# #     else:
#         print("invalid choice")



# queue=[]

# while True:
#     print("\n1.enqueue 2.dequeue 3.peek 4.display 5.exit")
#     choice=int(input("enter choice:"))
#     if choice==1:
#         val=int(input("enter value"))
#         queue.append(val)
#         print("added",val)
#     elif choice==2:
#         if not queue:
#             print("queue empty")
#         else:
#             print("poped",queue.pop())
#     elif choice==3:
#         if not queue:
#             print("queue empty")
#         else:
#             print("front:",queue[0])
#     elif choice==4:
#         print("Queue",queue)
#     else:
#         print("invaid choice")

# | Type           | Insert      | Delete      | Special Feature       |
# | -------------- | ----------- | ----------- | --------------------- |
# | Simple Queue   | Rear        | Front       | FIFO                  |
# | Circular Queue | Rear        | Front       | Reuses space          |
# | Priority Queue | By priority | By priority | Important items first |
# | Deque          | Both ends   | Both ends   | Flexible              |
        


size = 5
queue = [None] * size
front = -1
rear = -1

def enqueue(value):
    global front, rear
    
    if (rear + 1) % size == front:
        print("Queue Full")
        return
    
    if front == -1:
        front = 0
    
    rear = (rear + 1) % size
    queue[rear] = value
    print(value, "inserted")

def dequeue():
    global front, rear
    
    if front == -1:
        print("Queue Empty")
        return
    
    removed = queue[front]
    
    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size
    
    print(removed, "removed")

def display():
    if front == -1:
        print("Queue Empty")
        return
    
    i = front
    print("Queue elements:")
    
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % size
    print()

while True:
    print("\n1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        enqueue(value)

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")


















