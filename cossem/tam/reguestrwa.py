from dataclasses import dataclass
from random import randint
import requests

@dataclass
class ToDo:
   userId: int
   id: int 
   title: str 
   complete: bool

def convert_dict_to_todo(row: dict) -> ToDo:
    return ToDo(userId = row['userId'], id = row["id"], title = row['title'], complete = row['completed'])


def fetch_todo_list(url: str) -> list[dict]:
    res = requests.get(url)
    #print(res.status_code)

    return res.json()

def get_todos_of_user(todos: list[ToDo], user_id: int) -> str:
    return f'User id={user_id} wykonał {sum([t.complete for t in todos if t.userId == user_id])} na {len([t for t in todos if t.userId == user_id])}'

if __name__ == '__main__':
    tt = fetch_todo_list(url='https://jsonplaceholder.typicode.com/todos')
    todos = [convert_dict_to_todo(row) for row in tt]


    print("----------------------")
    print(get_todos_of_user(todos=todos, user_id=6))


