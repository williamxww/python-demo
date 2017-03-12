import time, datetime;

one_day = datetime.timedelta(days=1)
one_week = datetime.timedelta(weeks=1)
one_minute = datetime.timedelta(minutes=1)
one_seconds = datetime.timedelta(seconds=1)


def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    print(one_day)
