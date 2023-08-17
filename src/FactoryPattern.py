"""
Create time: 2023.08.17
Author: Lns-XueFeng
Goal: To master the common design pattern
"""


# 工厂模式
# 工厂模式是一个在软件开发中用来创建对象的设计模式，工厂函数根据不同输入来产生相适应的对象
class Person:
    def __init__(self):
        self.name = None
        self.gender = None
        self.age = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender


class Men(Person):
    def __init__(self, name):
        print("Hello Men" + name)


class Women(Person):
    def __init__(self, name):
        print("Hello Women" + name)


class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Men(name)
        if gender == 'W':
            return Women(name)


factory = Factory()
person = factory.getPerson("Lns-XueFeng", "M")
