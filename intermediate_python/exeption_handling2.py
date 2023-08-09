"""exeception


    Raises:
        e: contents of file

    Returns:
        _type_: error
"""

filename = input('enter the file name with extention: ')

def read_file(filename):
    """_summary_

    Args:
        filename (_type_): _description_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
    """
    try:
        with open(filename,'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError as e:
        raise e 

print(read_file(filename))
