#Name : Priyansu Nagchowdhary
#Reg. no. : 2141014004
def is_perfect_square(n):
    sqrt = int(n ** 0.5)
    return sqrt * sqrt == n
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
def find_numbers_in_range(start, end):
    result = []
    for num in range(start, end + 1):
        if is_perfect_square(num) and sum_of_digits(num) < 10:
            result.append(num)
    return result

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
numbers = find_numbers_in_range(start, end)
if numbers:
    print("Numbers in the range with sum of digits less than 10 and perfect squares:", numbers)
else:
    print("No numbers found in the given range that satisfy the conditions.")
