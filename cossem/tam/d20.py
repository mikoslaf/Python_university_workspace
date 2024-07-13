from random import randint
import concurrent.futures
import string
 

def get_simple_average_of_d6(n_throws: int) -> float:
    """
    Return the average value in throws of a 1,2,...5,6 die (kostka).

    :param n_throws:
    :return:
    """
    # wygenerować `n_throws` liczb całkowitych z przedziału [1,6]; policzyć sumę i zwrócić suma/n_throws

    return sum([randint(1, 6) for i in range(n_throws)])/n_throws

# def get_stop_on_1_d20() -> int:
#     table = [randint(1, 20) for _ in range(10)]
#     return len([i for i in table if i == 1])

# def get_statistic_d20(n_throws: int) -> float:
#     return (sum([get_stop_on_1_d20() for _ in range(n_throws)])/n_throws)*10

# zadanie dla entuzjastów 

def get_d6_map(map_len: int) -> int:
    i = 0
    current = 0
    while current != map_len:
        i += 1
        current += randint(1,6)
        if current > map_len:
            current = map_len * 2 - current
    return i

def get_statistic_d6_map6(n_throws: int) -> float:
    return sum([get_d6_map(10) for _ in range(n_throws)])/n_throws


# zadanie domowe 

def get_d6_map_basic(map_len: int) -> int:
    i = 0
    current = 0
    while current <= map_len:
        i += 1
        current += randint(1,6)
    return i

def get_statistic_d6_map6_basic(n_throws: int) -> float:
    return sum([get_d6_map_basic(10) for _ in range(n_throws)])/n_throws

# koniec zadania domowego 

def get_statistic_d20(n_throws: int) -> float:
    return (sum([len([i for i in [randint(1, 20) for _ in range(10)] if i == 1]) for _ in range(n_throws)])/n_throws)*10

def get_simple_average_of_2x_d6(n_throws: int) -> float:
    return sum([sum([randint(1, 6) for _ in range(2)]) for _ in range(n_throws)])/n_throws

# zad 1 

def get_count_to_reach_position(position: int, n_rolls: int) -> int:
    current = 0
    for _ in range(n_rolls):
        current_roll = randint(1,6)
        if current_roll == 6:
            current = 0
        else:
            current += randint(1,6)
        if current == position:
            return 1
    return 0

# zad A

def get_succes_reach_posiotion(position: int, n_rolls: int) -> int:
    current = 0
    for _ in range(n_rolls):
        current_roll = randint(1,6)
        if current_roll == 6:
            current = 0
        else:
            current += randint(1,6)
        if current == position:
            return 1
    return 0

def get_chance_to_reach_position(position: int, n_rolls: int) -> float:
    return (sum([get_succes_reach_posiotion(position, n_rolls) for _ in range(1000)])/1000)*100

# zad B

def c():
    with open('lal.txt', 'r+', encoding="utf8") as f:
        lines = f.readlines()
    dst = dict()
    for ln in lines:
        ln = ln.lower().strip()
        # ln = ln.replace('-', ' ').replace('!', ' ').replace('?', ' ').replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('\"', ' ').replace('\)', ' ').replace('\(', ' ')
        ln = ln.replace('„', ' ').replace('”', ' ').replace('…', ' ').replace('—', ' ').replace('–', ' ')
        ln = ln.translate(str.maketrans('', '', string.punctuation))
        words = ln.split(' ')
        for x in words:
            if x in dst:
                dst[x] += 1
            else:
                dst[x] = 1
    print(dict(sorted(dst.items())))




if __name__ == '__main__':
    # throws = [randint(1, 6) for i in range(10)]
    # print(throws)
    #print(get_simple_average_of_d6(n_throws=10000))
    # print(get_statistic_d20(n_throws=10000))
    # print(get_simple_average_of_2x_d6(n_throws=1000))
    # print(get_statistic_d6_map6(n_throws=1000))
    # print(get_statistic_d6_map6_basic(n_throws=1000))
    #print(get_chance_to_reach_position(20, 100))
    c()