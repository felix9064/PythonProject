#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def who_am_i(self):
        return 'I am a Student, my name is %s' % self.name

s = Student("felix", "Male", 99)

print(dir(s))
print(list(filter(lambda x: x[:2] != "__" and x[-2:] != "__", dir(s))))
