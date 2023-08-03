filename = input('enter the file name with extention: ')

def read_file(filename):
    try:
        with open(filename,'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError as e:
        raise e 

print(read_file(filename))
