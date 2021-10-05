# coding: utf-8
# license: GPLv3
from random import randint


class Attacker:
    _health = None
    _attack = None

    def attack(self, target):
        target._health -= self._attack * (randint(5, 20) / 10)

    def is_alive(self):
        return self._health > 0
