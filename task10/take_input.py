
def check_name(name):
    if str(name).isalpha():
        return True
    else:
        return False

def check_mail(email):
    if '@' in email:
        return True
    else:
        return False



if __name__ == '__main__':
    name = input('Please enter your name: ')
    if check_name(name):
        email = input('Please enter your mail: ')
        if check_mail(email):
            print('welcome')
        else:
            print('you input invalid mail')
    else:
        print('you input invalid name')