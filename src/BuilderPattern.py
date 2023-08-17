"""
Create time: 2023.08.17
Author: Lns-XueFeng
Goal: To master the common design pattern
"""


# 建造者模式
# 将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示
from abc import ABCMeta, abstractmethod


class Builder():  # 创造者
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_left_arm(self):
        pass

    @abstractmethod
    def draw_right_arm(self):
        pass

    @abstractmethod
    def draw_left_foot(self):
        pass

    @abstractmethod
    def draw_right_foot(self):
        pass

    @abstractmethod
    def draw_head(self):
        pass

    @abstractmethod
    def draw_body(self):
        pass


class Thin(Builder):  # 创造者
    def draw_left_arm(self):
        print("画左手")

    def draw_right_arm(self):
        print("画右手")

    def draw_left_foot(self):
        print("画左脚")

    def draw_right_foot(self):
        print("画右脚")

    def draw_head(self):
        print("画头")

    def draw_body(self):
        print("画瘦身体")


class Fat(Builder):  # 创造者
    def draw_left_arm(self):
        print("画左手")

    def draw_right_arm(self):
        print("画右手")

    def draw_left_foot(self):
        print("画左脚")

    def draw_right_foot(self):
        print("画右脚")

    def draw_head(self):
        print("画头")

    def draw_body(self):
        print("画胖身体")


class Director():  # 指挥者
    def __init__(self, person):
        self.person = person

    def draw(self):
        self.person.draw_left_arm()
        self.person.draw_right_arm()
        self.person.draw_left_foot()
        self.person.draw_right_foot()
        self.person.draw_head()
        self.person.draw_body()


thin = Thin()
fat = Fat()
director_thin = Director(thin)
director_thin.draw()
director_fat = Director(fat)
director_fat.draw()