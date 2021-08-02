def round_half_up(n):
    if n % 2 == 1:
        return int(n/2) + 1
    else:
        return int(n/2)
def divide_strings(a,b):
    a_front = a[:round_half_up(len(a))]
    a_back = a[round_half_up(len(a)):]
    b_front = b[:round_half_up(len(b))]
    b_back = b[round_half_up(len(b)):]
    return a_front + b_front + a_back + b_back
if __name__ == '__main__':#
    print(divide_strings('smile','good'))