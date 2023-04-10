print("For the following form please provide values accordingly")
print("x x+h x+2h ..... x+nh")
print("y0 y1 y2 ..... yn")
n = int(input("Enter the value of n: "))
x_values = []
y_values = []
for i in range(n):
    x_value = int(input(f"Enter the value of x_{i}: "))
    x_values.append(x_value)
    y_value = int(input(f"Enter the value of y_{i}: "))
    y_values.append(y_value)
print("Accepted values of x and y:")

# Print headers
print(f"{'x':<10} {'y':<10}")
print("-" * 20)

# Loop through pairs of x and y values and print them
for x, y in zip(x_values, y_values):
    print(f"{x:<10} {y:<10}")
print("Select of the options")
a=int(input("1)Forward Differences table\n2)Backwards Differences table"))


if a==1:
   
   print("Delta 1")
   row2 = []
   for i in range(1, n):
       diff2 = y_values[i] - y_values[i - 1]
       row2.append(diff2)
   for j in range(0,n-1):
       print(row2[j])
       
   print("Delta 2")
   row3 = []
   for i in range(1,n-2):
       diff3 = row2[i] - row2[i - 1]
       row3.append(diff3)
       print(row3)
       row2 = row3.copy()
       row3 = []
