from dataclasses import dataclass

@dataclass
class Lecture:
    przedmiotid: int
    nazwa: str
    active: bool

@dataclass
class Teacher:
    wykladowcaid: int
    imie: str
    nazwisko: str
    sid: int = -1
    prefix: str = ''
    suffix: str = ''
    active: bool = True

@dataclass
class Plan: 
    group_id: int
    lecture_id: int
    room: str
    hour: str
    day_of_week: str