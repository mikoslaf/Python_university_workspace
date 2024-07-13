from datetime import datetime


def log_datetime(func):
    '''Log the date and time of a function'''

    def wrapper():
        #print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        st = datetime.now().timestamp()

        func()

        en = datetime.now().timestamp()
        print(f'Function: {func.__name__}. Execution time: {en - st:.4f}s')
        func()
    return wrapper