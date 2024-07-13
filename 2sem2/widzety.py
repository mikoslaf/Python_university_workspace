import math

# screeen 3 x 5
def get_minimum_screen_count(m_small_titles: int, m_large_titles: int) -> int:
    widget = m_large_titles / 2 
    if(m_small_titles <= widget * 7):
        return math.ceil(widget)
    
    return math.ceil((m_small_titles + widget * 8) / 15)


if __name__ == '__main__':

    test_cases = [
    (1, 1, 1),
    (7, 2, 1),
    (12, 4, 2),
    (0, 3, 2),
    (1, 0, 1),
    (8, 1, 1),
    (0, 0, 0),
    (2, 0, 1),
    (15, 0, 1),
    (8, 2, 2),
    (0, 9, 5)
    ]
    
    for x, y, expected in test_cases:
        print(get_minimum_screen_count(m_small_titles=x, m_large_titles=y) == expected)