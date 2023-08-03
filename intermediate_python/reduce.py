from functools import reduce
def concatenate_strings(list_str):
    req_string = reduce(lambda x,y : x+y,list_str)
    return req_string

str_list = ['heelo','my','name']
print(concatenate_strings(str_list))