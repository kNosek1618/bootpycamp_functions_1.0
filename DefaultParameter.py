
def add(a,b):
    return a+b

print(add(2,3)) # 5

################

# DEFAULT VALUE
def add(a=0,b=0):
    return a+b

print(add()) # 0

# # # RESULT # # #
# DEFAULT VALUE CAN PROTECT AGAINST ERROR

def show_information(first_name='Konrad', is_musician=False):
    if first_name == 'Konrad' and is_musician:
        return "Welcome back Musician Konrad"
    elif first_name == 'Konrad':
        return "I really thought you were an musician..."
    return f"Hello {first_name}!"

print(show_information())
# I really thought you were an musician...

print(show_information(is_musician=True))
# Welcome back Musician Konrad

print(show_information('Marian'))
# Hello Marian!
