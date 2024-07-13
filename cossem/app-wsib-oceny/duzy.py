
from copy import deepcopy
from typing import Callable # kopiuje nowe obiekty, tworzy nowe instacje danych w środku 
from model import *
import requests
import operator
import hashlib

def md5(string):
    md5 = hashlib.md5()
    md5.update(string.encode())
    return md5.hexdigest()

def LoadClass(clas: object, url: str) -> list:
    res = requests.get(url)
    if res.status_code == 200:
        lectures = res.json()
        nice_lectures = [clas(**l) for l in lectures]
        return nice_lectures
    return []

def get_lectures() -> list[Lecture]:
    return LoadClass(Lecture, 'https://wddata.wsi.edu.pl/lectures?active=true&wdauth=0bfcf58b-6e48-494a-9821-06930ce213da')

def get_teachers() -> list[Teacher]:
    return LoadClass(Teacher, 'https://wddata.wsi.edu.pl/teachers?wdauth=0bfcf58b-6e48-494a-9821-06930ce213da')

def login(album: int, password: str) -> str:
    res = requests.get(f'https://wdauth.wsi.edu.pl/auth?album={album}&pass={md5(password)}')
    if res.status_code == 200:
        return res
    return 'Login Error'

def get_plan() -> list:
    return [
        Plan(group_id=1, lecture_id=1, room='S23', hour='12:00:00', day_of_week='Sat'),
        Plan(group_id=1, lecture_id=3, room='S12', hour='15:30:00', day_of_week='Sat'),
        Plan(group_id=1, lecture_id=2, room='L42', hour='13:45:00', day_of_week='Sat')
    ]

def display_plan_for_group(group_id: int) -> str:
    plan = [currect_plan for currect_plan in get_plan() if currect_plan.group_id == group_id]
    return sorted(plan, key=operator.attrgetter('hour'))

def lecture_choice(lectures: list[Lecture], search_query: str) -> list[Lecture]:
    plan = [lecture for lecture in lectures if search_query.lower() in lecture.nazwa.lower()]
    return sorted(plan, key=operator.attrgetter('nazwa'))

def teacher_choice(Teachers: list[Teacher], search_query: str) -> list[Teacher]:
    plan = [Teacher for Teacher in Teachers if search_query.lower() in Teacher.nazwisko.lower()]
    return sorted(plan, key=operator.attrgetter('nazwisko'))
    #return plan.sort(key=lambda lec: lec.nazwa)

def entity_selector(entities: list, choice_restrictor: Callable[[list, str], list]) -> int:

    selected = deepcopy(entities)

    while True:
        for item in selected:
            print(item)
        print("-------")
        query = input('> ')
        if query.startswith('*'):
            print('Choice selected')
            return int(query[1:])
        else:
            selected = choice_restrictor(selected, query)


if __name__ == '__main__':
    l1 = Lecture(przedmiotid=111, nazwa='Technika cyfrowa', active=True)
    l2 = Lecture(przedmiotid=29, nazwa='Język angielski', active=True)
    l3 = Lecture(przedmiotid=17, nazwa='Grafika 2d', active=True)
    l4 = Lecture(przedmiotid=94, nazwa='Kompetencje interpersonalne', active=True)

    lectures = [l1, l2, l3, l4]

    t1 = Teacher(wykladowcaid=6, imie='Abra', nazwisko='Kadabra')
    t2 = Teacher(wykladowcaid=61, imie='Abra1', nazwisko='Kadabra1')
    t3 = Teacher(wykladowcaid=16, imie='Abra2', nazwisko='Kadabra2')
    t4 = Teacher(wykladowcaid=66, imie='Abra3', nazwisko='Kadabra')

    teachers = [t1, t2, t3, t4]

    print("------")
    id_lectures = entity_selector(lectures, lecture_choice)
    print("------")
    id_teachers = entity_selector(teachers, teacher_choice)
    print("------")
    

    # lectures = get_lectures()
    # teachers = get_teachers()
    # for nl in display_plan_for_group(1):
    #      print(nl)
    #print(login('4097', 'haslo'))

