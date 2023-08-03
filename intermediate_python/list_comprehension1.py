list_input = input('enter multiple strings separated by spaces: ')
list_of_strings = list_input.split(" ")

required_list = [string for string in list_of_strings if len(string)>5]
print(required_list)