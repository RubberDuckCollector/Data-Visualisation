num_list = []

x_axis = []
y_axis = []

for x in range(1, 101):
    
    y = x
    count = 0

    x_axis.append(x)
    
    while x != 1:
    
        if x % 2 == 0:
            x /= 2
            count += 1
        elif x % 2 != 0:
            x = x * 3 + 1
            count += 1
            
    num_list.append([y, count])
    y_axis.append(count)

print(num_list)
print("\n")

print(x_axis)

print("\n")

print(y_axis)

print("\n")
print(f"{x_axis[87] = }")
print(f"{y_axis[87] = }")

