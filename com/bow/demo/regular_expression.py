import re


def find(pattern, file_name):
    f = open(file_name)
    p = re.compile(pattern)
    for l in f:
        m = p.search(l)
        if m is not None:
            print(l)


def search(pattern, file_name):
    f = open(file_name)
    for l in f:
        m = re.search(pattern, l)
        if m is not None:
            print(l, m.group())


def find_all(pattern, file_name):
    result = []
    f = open(file_name)
    for l in f:
        a = re.findall(pattern, l)
        if a is not None:
            result.extend(a)
    print(result)


find_all("\d+", "test.txt")
