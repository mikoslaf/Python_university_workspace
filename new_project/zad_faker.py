from datetime import datetime
from faker import Faker
from dataclasses import dataclass

@dataclass
class Person:
    pesel: str
    name: str
    phone: str
    adres: str

def get_random_person() -> Person:
    fake = Faker(['pl_PL'])
    new_pesel = fake.pesel()
    new_name = fake.name()
    new_phone = fake.phone_number()
    new_adres = fake.address()
    if not ',' in new_pesel and not ',' in new_name and not ',' in new_phone and not ',' in new_adres: 
        return Person(pesel=new_pesel, name=new_name, phone=new_phone, adres=new_adres)
    else:
        return get_random_person()
    
def gen_random_ppl(n: int) -> list[Person]:
    return [get_random_person() for _ in range(n)]

@staticmethod
def to_csv(person: 'Person') -> str:
    file = open("data.csv", 'w+')
    result = ''
    for x in person:
        for y in x.__dict__:
            result += str(y) + ","
    file.write(result)
    file.close()
    return result

@staticmethod
def from_csv(line: str) -> 'Person': 
    pass   

def ts() -> float:
    return datetime.now().timestamp()


if __name__ == '__main__':
    start_ts = ts()
    peaple = gen_random_ppl(10** 2)
    end_ts = ts()
    print(f'generating ppl took {end_ts - start_ts:.3f}s')
    for x in peaple:
        to_csv(peaple)