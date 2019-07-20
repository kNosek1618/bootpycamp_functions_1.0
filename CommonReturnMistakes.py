
# TWO OPTIONS FOR DEFINE IF STATEMENT WITH RETURN METHOD
def is_odd_number(num):
    if num % 2 != 0:
        return True
    else:
        return False

print(is_odd_number(4))
print(is_odd_number(9))

###########################

# IN FUNCTION LIKE THIS 'ELSE' IS UNNECESSARY
def is_odd_number(num):
    if num % 2 != 0:
        return 'TRUE'
    return 'FALSE'

print(is_odd_number(4))
print(is_odd_number(9))