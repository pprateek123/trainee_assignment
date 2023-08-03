input_num = input('enter a number: ')

def read_int(num):
    try:
        return int(num)
    except ValueError:
        print('input cannt be converted to zero')

print(read_int(input_num))