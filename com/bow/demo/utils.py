import time


def is_number(num):
    if isinstance(num, (int, float, complex)):
        return True
    else:
        return False


def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    print(get_current_time())
