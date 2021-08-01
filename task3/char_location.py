def char_locations(word,searced_char):
    return [index for index, char in enumerate(word) if char == searced_char]



if __name__ == '__main__':
    print(char_locations('abdoooo','o'))