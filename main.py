#
#   Copyright © 2023, SnowCoder404
#
def file_open():
    file = open('test.txt', 'r')
    file = file.read().lower()
    crypt(file=file)


def crypt(file):
    file = file.replace('a', '10')
    file = file.replace('b', '20')
    file = file.replace('c', '30')
    file = file.replace('d', '40')
    file = file.replace('e', '50')
    file = file.replace('f', '60')
    file = file.replace('g', '70')
    file = file.replace('h', '80')
    file = file.replace('i', '90')
    file = file.replace('j', '100')
    file = file.replace('k', '110')
    file = file.replace('l', '120')
    file = file.replace('m', '130')
    file = file.replace('n', '140')
    file = file.replace('o', '150')
    file = file.replace('p', '160')
    file = file.replace('q', '170')
    file = file.replace('r', '180')
    file = file.replace('s', '190')
    file = file.replace('t', '200')
    file = file.replace('u', '220')
    file = file.replace('v', '230')
    file = file.replace('w', '240')
    file = file.replace('x', '250')
    file = file.replace('y', '260')
    file = file.replace('z', '270')
    file = file.replace('?', '280')
    file = file.replace('!', '290')
    file = file.replace('@', '300')
    file = file.replace(',', '310')
    file = file.replace('\'', '320')
    file = file.replace('.', '330')
    file = file.replace('(', '340')
    file = file.replace(')', '350')
    file = file.replace('=', '360')
    print(file)


file_open()
