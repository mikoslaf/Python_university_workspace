from string import ascii_lowercase
import pytest

def find_best_purchase(n: int, a: int, b: int) -> int:
    discount = n%2 * a + (n - n%2)//2 * b
    normal = n * a
    if(discount < normal):
        return discount
    return normal

def find_missing_and_surplus_parts(need: str, have: str) -> tuple[str,str]:

    dict_need = {element:0 for element in need}
    dict_have = {element:0 for element in have}
    dict_need.update(dict_have)

    for x in need:
        dict_need[x] += 1
    for x in have:
        dict_have[x] += 1

    result_need = ''
    result_have = ''
    for k,x in dict_need.items():
        if k in dict_have:
            if dict_need[k] < dict_have[k]:
                for _ in range(dict_have[k] - dict_need[k]):
                    result_have += k
            else:
                for _ in range(dict_need[k] - dict_have[k]):
                    result_need += k
        else:
            for _ in range(x):
                result_need += k

    return result_need, result_have

def test_simple():
    print(find_best_purchase(1, 10, 15) == 10)
    print(find_best_purchase(2, 10, 15) == 15)
    print(find_best_purchase(4, 3, 5) == 10)
    print(find_best_purchase(5, 3, 5) == 13)
    print(find_best_purchase(4, 3, 10) == 12)
    print(find_best_purchase(5, 3, 10) == 15)

def test_simple():
    missing, surplus = find_missing_and_surplus_parts('ab', 'b')
    assert missing == 'a'
    assert surplus == ''


def test_simple2():
    missing, surplus = find_missing_and_surplus_parts('ab', 'aab')
    assert missing == ''
    assert surplus == 'a'


def test_bulk():
    assert find_missing_and_surplus_parts('ab', 'abc') == ('', 'c')
    assert find_missing_and_surplus_parts('aaaabbbb', 'aaaabbbc') == ('b', 'c')
    assert find_missing_and_surplus_parts('abbc', 'abc') == ('b', '')

if __name__ == '__main__':
    print(find_missing_and_surplus_parts("ab","b"))
    print(find_missing_and_surplus_parts("ab","aab"))
    print(find_missing_and_surplus_parts("ab","abc"))
    print(find_missing_and_surplus_parts('aaaabbbb', 'aaaabbbc'))
    print(find_missing_and_surplus_parts('abbc', 'abc'))

    my_dictionary = {element:0 for element in ascii_lowercase}
    
    for x in 'kadabra':
        my_dictionary[x] += 1

    print(my_dictionary)