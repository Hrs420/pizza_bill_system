print("Welcome to Python Pizza Deliveries ")
size = input("Enter your Pizza Size? S, M, L ")

extra_cheese = input("Do you want extra cheese? Y or N")
bill = 0
if(size == "S"):
  bill += 15
  print(f"Your Bill is : {bill}")
elif size == "M":
  bill += 20
  print(f"Your Bill is : {bill}")
elif size == "L":
  bill += 25
  print(f"Your Bill is : {bill}")

add_pepperoni = input("Do you want pepperoni ? Y or N")
if add_pepperoni == "Y" :
  if size == "S":
    bill += 2
  else:
    bill +=3

if extra_cheese == "Y":
  bill+=1



print(f"Your Bill is ${bill} ")
