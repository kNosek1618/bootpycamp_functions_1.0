
total = 0

def increment():
    global total
    total += 1
    return total

print(increment()) # 1

# # # RESULT # # #
# IF WE USE A 'GLOBAL' METHOD, THEN WE CAN USE A VARIABLE FROM OUTSIDE FUNCTION

