import matplotlib.pyplot as plt

# create the y-axis data, which is a list of the squares of the numbers from 1 to 100
y_axis = [i**2 for i in range(100)]

# create the x-axis data, which is a list of the numbers from 1 to 100
x_axis = [i for i in range(100)]

# create a plot using the x and y axis data
plt.plot(x_axis, y_axis)

plt.xlabel("numbers from 1 to 100")
plt.ylabel("numbers on the x axis squred, the square numbers")
plt.title("the square numbers")
plt.show()
