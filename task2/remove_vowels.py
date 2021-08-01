def rem_vowel(word):
    vowels = ['a','e','i','o','u']
    result = [l for l in word if l.lower() not in vowels]
    result = ''.join(result)
    print(result)


if __name__ == '__main__':
    rem_vowel('Mobile')