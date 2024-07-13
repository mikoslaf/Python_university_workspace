from random import randint
from faker import Faker

def get_persons() -> list[str]:
    return [Faker(['pl_PL']).name().lower() for _ in range(1, 10)]

def game(a_min: int, a_max: int, n_attempts: int,  attempt: int = 1, secret_number: int = 0): # nie działa jak coś
    if secret_number == 0:
        secret_number = randint(a_min, a_max)
    if attempt > n_attempts:
        print(f"Not today! You triing to find {secret_number} guess is {a_max//2 + a_min}")
        return
    print(f'attempt ({attempt}/{n_attempts})')
    guess = a_max//2 + a_min
    if guess > secret_number:
        print('szukana liczba jest mniejsza')
        game(a_min=a_min, a_max=guess, n_attempts=n_attempts, attempt=attempt+1, secret_number=secret_number)
    elif guess < secret_number:
        print('szukana liczba jest większa')
        game(a_min=guess, a_max=a_max, n_attempts=n_attempts, attempt=attempt+1, secret_number=secret_number)
    else:
        print('trafione! brawo!')
        return

def find_person_by_name(persons: list[str], name: str) -> str: # też coś nie działa, pobrać z githuba od wykładowcy
    if persons[0] >= name:
        return persons[0]
    b_min = 0
    b_max = len(persons)
    while True:
        b = (b_max + b_min) // 2
        if persons[b] < name:
            b_min = b
        else:
            b_max = b
        if b_max-b_min  <= 1:
            break
    return persons[b]

def find_bok(a: int, b: int) -> int:
    pass

if __name__ == '__main__':
    # game(a_min=1, a_max=1000, n_attempts=10)
    # ludzie = get_persons()
    # print(ludzie)
    # print(ludzie.sort())
    print("d")