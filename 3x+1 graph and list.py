import matplotlib.pyplot as plt

x_axis = []
y_axis = []

for x in range(1, 101):
    
    y = x
    count = 0 # count is also the y axis, it's the stoppng time of each number which is plotted on th y axis

    x_axis.append(x)
    
    while x != 1:
        if x % 2 == 0:
            x /= 2
            count += 1
        elif x % 2 != 0:
            x = x * 3 + 1
            count += 1

    y_axis.append(count)

num_list = []
for i in range(len(x_axis)):
    num_list.append([x_axis[i], y_axis[i]])

print(num_list)
print("\n")

print(x_axis)

print("\n")

print(y_axis)

plt.plot(x_axis, y_axis)
plt.xlabel("iterating variable, x")
plt.ylabel("number of steps to diminish down to 1, (stopping time), count")
plt.title("3x+1")
plt.show()
