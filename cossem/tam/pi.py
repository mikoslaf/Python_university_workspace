def make_pi2():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for _ in range(10000):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10 * q, 10 * (r - m * t), t, k, (10 * (3 * q + r)) // t - 10 * m, x
        else:
            q, r, t, k, m, x = q * k, (2 * q + r) * x, t * x, k + 1, (q * (7 * k + 2) + r * x) // (t * x), x + 2

def make_pi():
    my_array = []

    for i in make_pi2():
        my_array.append(str(i))

    my_array = my_array[:1] + ['.'] + my_array[1:]
    big_string = "".join(my_array)


    return big_string

def pi_zero():
    pi = make_pi()
    dist = {x:0 for x in range(10)}
    i = 0
    for x in str(pi)[2:]:
        x = int(x)
        if i != 0:
            if str(pi)[2:][i - 1] == "1":
                dist[x] += 1
        i += 1
    return(dist)

def get_pi_txt() -> str:
    with open('pi.txt') as f:
        lines = f.readlines()
        print(lines)

if __name__ == '__main__':
    print(get_pi_txt())
    

