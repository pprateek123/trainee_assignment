import string

alphabet_list = list(string.ascii_lowercase)

ascii_value = [ord(i) for i in alphabet_list]

req_dic = {k:v for k,v in zip(alphabet_list,ascii_value)}
print(req_dic)