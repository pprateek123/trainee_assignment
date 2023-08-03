import math



def filter_prime_numbers(num_list):
    is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, math.isqrt(num) + 1))
    req_list = list(filter(is_prime,num_list))
    return req_list
numbers = [2,3,4,7,13,41]
print(filter_prime_numbers(numbers))


