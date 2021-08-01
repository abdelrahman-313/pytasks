def remove_duplicates(elements):
    # set data structure can not contain any duplicates values
    return list(set(elements))


if __name__ == '__main__':
    print(remove_duplicates([1,2,2,3,3,4,2,5,4,4,6,4,3,2,1,7]))