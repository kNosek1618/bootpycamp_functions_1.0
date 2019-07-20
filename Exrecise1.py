
def generate_evens():
    numbers = []
    for i in range(1,50):
        if i % 2 == 0:
            numbers.append(i)
    return numbers

print(generate_evens())

# # # RESULT # # #
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
# ONLY EVEN NUMBERS
