# -*- coding:utf-8 -*-

from random import randint

class User:
    def __init__(self):
        self.win = 0
    def commit(self, q):
        return input(q)

class Enemy:
    def submit(self):
       return randint(1 ,3)
	