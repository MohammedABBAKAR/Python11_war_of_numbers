# Create a function that takes a list of integers, 
# sums the even and odd numbers separately, 
# then returns the difference between the sums of the even and odd numbers.
# Examples

# war_of_numbers([2, 8, 7, 5]) ➞ 2
# # 2 + 8 = 10
# # 7 + 5 = 12
# # 12 is larger than 10
# # So we return 12 - 10 = 2

# war_of_numbers([12, 90, 75]) ➞ 27

# war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]) ➞ 168
def war_of_numbers(numbers):
    even_sum = 0
    odd_sum = 0
    
    for number in numbers:
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number
    
    return abs(even_sum - odd_sum)

# Examples
print(war_of_numbers([2, 8, 7, 5]))  # ➞ 2
print(war_of_numbers([12, 90, 75]))  # ➞ 27
print(war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))  # ➞ 168


def war_of_numbers(lst):
    even_sum = sum(i for i in lst if i % 2 == 0)
    odd_sum = sum(i for i in lst if i % 2 != 0)
    return abs(even_sum - odd_sum)

# Examples
print(war_of_numbers([2, 8, 7, 5]))  # ➞ 2
print(war_of_numbers([12, 90, 75]))  # ➞ 27
print(war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))  # ➞ 168



