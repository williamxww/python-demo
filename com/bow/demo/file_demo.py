# file operation

import os


def read_file(file_url, result_url):
    try:
        file_input = open(file_url, 'r')
        file_output = open(result_url, 'w')
        for line in file_input:
            handle(line)
            file_output.write(line)
    except IOError as e:
        print(e)
    finally:
        file_input.close()
        file_output.close()


# check file is exists or not
def exists_file(file_name, directory):
    if os.path.exists(directory):
        os.path.lis
    else:
        raise RuntimeError('directory do not exists')


# used to handle each line in file
def handle(line):
    print(line)


if __name__ == '__main__':
    read_file('test.txt', 'result.txt')
    print('------END----------')
