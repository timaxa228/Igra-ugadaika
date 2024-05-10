from random import *

print('Добро пожаловать в числовую угадайку')


def is_valid(num):
    if num.isdigit():
        return True
    else:
        return False


def max_range():
    while True:
        a = input('Введите максимальное возможное число: ')
        if not is_valid(a) or int(a) < 0:
            print(f'Введите целое число больше нуля!')
            continue
        return int(a)


n = max_range()
chislo = randint(0, n)


def get_num():
    while True:
        num = input('Введите предполагаемое число: ')
        if not num.isdigit() or not (0 <= int(num) <= n):
            print(f'А может быть все-таки введем целое число от 0 до {n}?')
            continue
        return int(num)


def ugadaika():
    cnt = 0
    print(f'Загаданное число будет от 0 до {n}')
    while n != chislo:
        a = get_num()
        cnt += 1
        if a < chislo:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        if a > chislo:
            print('Ваше число больше загаданного, попробуйте еще разок')
        if a == chislo:
            print('Вы угадали, поздравляем!')
            print(f'Вам потребовалось {cnt} попыток')
            break


while True:
    ugadaika()
    while True:
        print('Отличная игра, сыграем ещё раз?')
        vvod = input('Продолжаем - да, заканчиваем - нет: ')
        if vvod == 'да':
            n = max_range()
            chislo = randint(0, n)
        if vvod == 'нет':
            print('Игра окончена')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        break
    break
