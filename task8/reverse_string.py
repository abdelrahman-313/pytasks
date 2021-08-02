def reverse_string(word):
    word_list = list(word)
    word_list.reverse()
    return ''.join(word_list)


if __name__ == '__main__':
    print(reverse_string('google'))