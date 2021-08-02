def division_decision(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "buzz"


if __name__ == '__main__':
    print(division_decision(15))