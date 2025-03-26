
while True:
 x = input("Enter X: ")
 y = input("Enter Y: ")


# convert string to number

 try:
   num_x = float(x)
   num_y = float(y)
   print(num_x / num_y)
 except:
      print("Invalid input")







