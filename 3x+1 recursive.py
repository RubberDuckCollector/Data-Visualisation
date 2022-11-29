count = 0

def collatz_conjecture(x):

    global count

    if x == 1:
        return count
    elif x % 2 == 0:
        count += 1
        return collatz_conjecture(x / 2)
    else:
        count += 1
        return collatz_conjecture(x * 3 + 1)

print(collatz_conjecture(100))
