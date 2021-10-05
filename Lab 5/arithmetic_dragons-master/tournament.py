# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *
from datetime import datetime
from time import sleep

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print("\033[H\033[J")
        print('Вышел', dragon._color, 'дракон!')
        start_dragon_time = datetime.now()
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли ** \n ** вы оставили дракону {} здоровья **'.format(dragon._health))
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... ** \n ** дракон оставил вам {} здоровья **'.format(hero._health))
        if dragon.is_alive():
            break
        experience = round(100 / (datetime.now() - start_dragon_time).seconds)
        print('Дракон', dragon._color, 'повержен! Вам начисленно {} опыта\n'.format(experience))
        hero.add_experience(experience)
        sleep(3)

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 3
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 3)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
