from array import array
def generate_array(length,start):
    generated_list = range(start,length)
    return array('i',generated_list)


if __name__ == '__main__':
    print(generate_array(5,0))