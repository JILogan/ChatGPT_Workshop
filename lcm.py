def lcm(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

# test the function
print(lcm(4, 6)) # 12
print(lcm(15, 17)) # 255
