
from AAltimated_decorator import log_datetime
from random import randint, seed

def gen_network_traffic(n_packets: int) -> list[int]:
    return [randint(0, 10) for _ in range(n_packets)]

def find(table: list[int], param_range: int):
    current_sum = sum([x for x in table[:param_range]])
    result = [current_sum]
    for x in range(1, len(table) - param_range + 1):
        current_sum -= table[x - 1]
        current_sum += table[x + param_range - 1]
        result.append(current_sum)
    return max(result)

def sum_of_chars(word: str) -> int:
    return sum([ord(word[i]) * (i + 1) for i in range(len(word))]) % 107

if __name__ == '__main__':
    seed(111)
    print(sum_of_chars("abrakadabra"))
    #print(find(table= gen_network_traffic(60 * 60 * 24), param_range=3600))