string1 = "animal"
string2 = "human"

req_set = {i for i in set(string1) if i in set(string2)}

print(req_set)
