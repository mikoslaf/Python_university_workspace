from datetime import datetime

def get_final_amoeba_size(init_size: int, food: list[int]) -> int:
    food.sort()
    l_min = 0
    l_max = len(food)
    while True:
        y = (l_max + l_min) // 2 
        if food[y] == init_size:
            init_size *= 2
            l_min = 0
            l_max = len(food)
        if food[y] < init_size:
            l_min = y
        else: 
            l_max = y
        if l_min + 1 >= l_max:
            break
    return init_size

def get_final_amoeba_size2(init_size: int, food: list[int]) -> int:
    food.sort()
    while init_size in food: init_size *=2
    return init_size

def get_final_amoeba_size3(init_size: int, food: list[int]) -> int:
    food = set(food)
    for el in food:
        if init_size == el:
            init_size *= 2
    return init_size

def ts() -> float:
    return datetime.now().timestamp()

def is_necklace_beautiful(necklace: str) -> bool:
    start = 0
    while necklace.find("*", start) > 0:
        print("jest")
        start = necklace.find("*", start) + 1
        
    return necklace.find("N")

if __name__ == '__main__':
    #print(get_final_amoeba_size(3, [48,60,90,100,122,1,24,1,1,96,1,2,2,6,2,12,2,2,3]))
    #print(get_final_amoeba_size(3, [48,60,90,100,122,1,24,1,1,96,1,2,2,6,2,12,2,2,3]))
    #print(get_final_amoeba_size3(3, [48,60,90,100,122,1,24,1,1,96,1,2,2,6,2,12,2,2,3]))

    st = ts()

    #res = get_final_amoeba_size(2, [x for x in range(10**8)]) #13.58
    #res = get_final_amoeba_size2(2, [x for x in range(10**8)]) #15.12
    #res = get_final_amoeba_size3(2, [x for x in range(10**8)]) #16.1

    # res = is_necklace_beautiful("---*---*--")

    en = ts()
    #print(res)
    #print(f'execution time: {en - st:.4f}s')
    w = [1,2,3,4,5, 6,7]
    print(len(w))
    ile = 1000
    for b in range(10):
        ile = ile//2
        print(ile)
    