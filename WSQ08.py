def sum_numbers(x,y):
    answer = x + y
    return answer

def difference_numbers(x,y):
    answer = x - y
    return answer

def product_numbers(x,y):
    answer = x * y
    return answer

def division_numbers(x,y):
    answer = x // y
    return answer

def remainder_numbers(x,y):
    answer = x % y
    return answer


num1 = int(input("First Number"))
num2 = int(input("Second Number"))

the_sum = sum_numbers(num1,num2)
the_difference = difference_numbers(num1,num2)
the_product = product_numbers(num1,num2)
the_division = division_numbers(num1,num2)
the_remainder= remainder_numbers(num1,num2)


print ("The sum is",the_sum)
print ("The difference is",the_difference)
print ("The product is",the_product)
print ("The division is",the_division)
print ("The remainder is",the_remainder)
