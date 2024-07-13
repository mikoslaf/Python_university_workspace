import pytest

def get_log_2(x: float) -> float:
    if x <= 0:
        return 0
    min = 0 
    max = x
    while True:
        y = (max + min) / 2 
        if 2 ** y < x:
            min = y
        else: 
            max = y
        if min + 10 ** -5 >= max:
            break
    #print(min, max)
    #print(2 ** min,2 ** max)
    return y

if __name__ == '__main__':
    print(get_log_2(100))
    