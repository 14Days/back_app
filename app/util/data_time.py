import datetime


def get_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def shift_time(data: str) -> str:
    temp = data.split(' ')
    return temp[0]


