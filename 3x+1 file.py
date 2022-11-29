f = open("nums.txt", "w")




for x in range(1, 1001):
    
    count = 0
    
    f.write(f"{x}, ")
    
    while x != 1:
        
        if x % 2 == 0:
            x /= 2
            count += 1
        elif x % 2 != 0:
            x = x * 3 + 1
            count += 1
    
    
    f.write(f"{count}\n")

f.close()
