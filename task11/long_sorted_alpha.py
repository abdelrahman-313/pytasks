def get_long_sorted_alpha(word):
    long_alpha = word[0]
    compaired = word[0]
    for w in word[1:]:
        if ord(w) > ord(compaired):
            long_alpha += w
            compaired = w
        else:
            break
    return long_alpha

if __name__ == '__main__':
    print(get_long_sorted_alpha('abdulrahman'))