# -*- coding: UTF-8 -*-
import fileinput
import os


def create_file(file_name, content):
    # w 会创建一个新文件，以前存在就会覆盖
    f = open(file_name, "w")
    f.write(content)
    f.flush()
    f.close()


def show_content(file_name, line_num):
    f = open(file_name)
    # readlines一次性全部读入内存,
    lines = f.readlines()
    print(lines[line_num])
    f.close()


def show_all(file_name):
    f = open(file_name)
    for line in f:
        print(line.strip())
    f.close()


def file_replace(file_name, target, replace_content, backup):
    if backup:
        file_input = fileinput.input(file_name, inplace=1, backup=".bak")
    else:
        file_input = fileinput.input(file_name, inplace=1, backup="")
    for line in file_input:
        print(line.replace(target, replace_content).strip())
    file_input.close()


def show_iter(products):
    '''
    just for test
    :param a list or string
    :return:  nothing
    '''
    iterator = iter(products)
    for x in iterator:
        print(x)


def remove_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)
    else:
        print("only file can be removed with this function")


# file_replace("test.txt","b","A",False)
# show_content("test.txt",1)
# show_all("test.txt")
# show_iter(range(10))
# remove_file("test.txt")
create_file("test.txt", "123");